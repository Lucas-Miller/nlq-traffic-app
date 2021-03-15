from flask import Flask, render_template
main = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')