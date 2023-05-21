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
flask run --host 0.0.0.0 --port 3000
```

2. Open the app on http://0.0.0.0:3000

Here you will have two options: Random and Creator

### Random

Clicking on the `Random` button you will generate a random meme and it will be displayed on the app homepage

### Creator

Clicking on the `Creator` button you will have the option to input an image URL and a quote with the author name. If you then click on 'Create Meme!' the personalised meme will be shown on the homepage.

## CLI interface
Also the CLI interface allows to run the meme generator to generate a random meme or to generate a personalised meme

### Random
To generate a random meme simply run `python3 main.py` and the meme will be generated in the `/memes` folder. The file name will be printed on the shell. 

### Creator
Running `python3 main.py --help` will output the instructions for the optional arguments

```sh
$ python3 main.py --help
usage: main.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

meme generator parameters

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to an image file
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image
```


