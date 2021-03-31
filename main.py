from flask import Flask, render_template, request

import os
import collections
import json
import numpy as np
import scann
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
import tensorflow_text as text
import tensorflow_addons as tfa

import glob
import pickle

from helper_functions import find_matches

UPLOAD_FOLDER = 'image_data/uploads/'
main = Flask(__name__)

print("Loading vision and text encoders...")
vision_encoder = keras.models.load_model("models/vision_encoder-v3", compile=False)
text_encoder = keras.models.load_model("models/text_encoder-v3", compile=False)
print("Models are loaded.")

image_paths = glob.glob("static/image_data/images/*.jpg")


with open(r"static/image_data/image_embeddings.pickle", "rb") as input_file:
    image_embeddings = pickle.load(input_file)

@main.route('/')
def index():
    return render_template('index.html')


def image_folder(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

def compute_recall(neighbors, true_neighbors):
    total = 0
    for gt_row, row in zip(true_neighbors, neighbors):
        total += np.intersect1d(gt_row, row).shape[0]
    return total / true_neighbors.size

def find_matches_scann(image_embeddings, query_embedding, k=9, normalize=True):    
    # Normalize the query and the image embeddings.
    if normalize:
        image_embeddings = tf.math.l2_normalize(image_embeddings, axis=1)
        query_embedding = tf.math.l2_normalize(query_embedding, axis=1)
    # Create ScaNN searcher
    searcher = scann.scann_ops.builder(image_embeddings, 10, "dot_product").tree(
    num_leaves=2000, num_leaves_to_search=100, training_sample_size=60000).score_ah(
    2, anisotropic_quantization_threshold=0.2).reorder(100).build()

    # Use ScaNN to find top neighbors
    #results = searcher.search_batched(query_embedding)
    results = searcher.search_batched(query_embedding)
    return results[0][0]


@main.route('/get_query', methods=['POST'])
def get_query():
    nl_query = request.form['nl_query']
    print(nl_query)
    # Create Embeddings of query
    query_embedding = text_encoder(tf.convert_to_tensor([nl_query]))
    #query_embedding_normalized = tf.math.l2_normalize(query_embedding, axis=1)

    # Use scann module in python to finds closest embeddings
    # return those images 
    # display images 
    img = []
    img_results = find_matches_scann(image_embeddings, query_embedding, k=9, normalize=True)
    print(img_results[1])
    for i in range(0, 10): 
        img.append(image_paths[(img_results[i])])

    print(img[5])

    return render_template('results.html', img_results=img)




# Images need to be in some database 
# image embeddings line up with the photos

# Apache spark or apache beam to create a data pipeline that when new photoes are added to create embieddings for them
