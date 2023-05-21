"""
This module implements a Flask application for a meme generator.

The application allows users to generate random memes or create memes using their own images and quotes.

Routes:
- '/' (GET): Generate a random meme.
- '/create' (GET): User input for meme information.
- '/create' (POST): Create a user-defined meme.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from src.QuoteEngine import Ingestor
from src.MemeEngine import MemeEngine

app = Flask(
    __name__,
    static_folder='src/static',
    template_folder='src/templates'
)


meme = MemeEngine('src/static')


def setup():
    """Load all resources."""
    quote_files = ['./src/_data/DogQuotes/DogQuotesTXT.txt',
                   './src/_data/DogQuotes/DogQuotesDOCX.docx',
                   './src/_data/DogQuotes/DogQuotesPDF.pdf',
                   './src/_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./src/_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path.replace("src/", ""))


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        response = requests.get(image_url)
    except requests.exceptions.RequestException:
        abort(400, description="Invalid image URL")

    if response.status_code == 200:
        with open('src/tmp/tmp.jpg', 'wb') as f:
            f.write(response.content)
        img_path = 'src/tmp/tmp.jpg'
    else:
        abort(400, description="Invalid image URL")

    path = meme.make_meme(img_path, body, author)

    os.remove(img_path)

    return render_template('meme.html', path=path.replace("src/", ""))


if __name__ == "__main__":
    app.run()
