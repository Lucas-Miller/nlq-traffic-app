from flask import Flask, render_template, request

import os
import collections
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
import tensorflow_text as text
import tensorflow_addons as tfa

import glob
import pickle

from helper_functions import find_matches

main = Flask(__name__)

vision_encoder = keras.models.load_model("models/vision_encoder-v3")
text_encoder = keras.models.load_model("models/text_encoder-v3")

image_paths = glob.glob("image_data/images/*.jpg")


with open(r"image_data/image_embeddings.pickle", "rb") as input_file:
    image_embeddings = pickle.load(input_file)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/get_query', methods=['POST'])
def get_query():
    nl_query = request.form['nl_query']
    print(nl_query)

    # Create Embeddings of query

    # Use scann module in python to finds cloest embedings 
    # return those images 
    # display images 
    return render_template('index.html')




# Images need to be in some database 
# image embeddings line up with the photos

# Apache spark or apache beam to create a data pipeline that when new photoes are added to create embieddings for them
