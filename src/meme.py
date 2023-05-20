import os
import random
from .QuoteEngine import Ingestor, QuoteModel
from .MemeEngine import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./src/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        # print(f'the list is {imgs}')
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./src/_data/DogQuotes/DogQuotesTXT.txt',
                       './src/_data/DogQuotes/DogQuotesDOCX.docx',
                       './src/_data/DogQuotes/DogQuotesPDF.pdf',
                       './src/_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./memes/')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='meme generator parameters')
    parser.add_argument("--path", type=str, default=None,
                        help='path to an image file')
    parser.add_argument("--body", type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument("--author", type=str, default=None,
                        help='quote author to add to the image')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
    # print(generate_meme())
