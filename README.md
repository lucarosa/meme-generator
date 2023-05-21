# Meme Generator
Meme generator project for the Udacity Intermediate Python Nanodegree

# About The Project
Simple Python meme generator which includes a Flask app that allows to generate random memes or to generate memes using user provide image URL and text. It is also possible to interact with the meme generator using a CLI interface.

# Getting Started
To run the generator locally you will need to follow these simple steps

## Prerequisites
Install xpdf library

* On Mac
```brew install xpdf```

* On Linux
```sudo apt install -y xpdf```

## Installation
1. Clone the repo
```sh
git clone https://github.com/lucarosa/meme-generator.git
```

2. Create virtual environment and install requirements
```sh
cd meme-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Usage

## Flask app
To run the meme generator using the Flask web app follow these steps

1. Export app 
```sh
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
``

2. Open the app on http://0.0.0.0:3000

If 

