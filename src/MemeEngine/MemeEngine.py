"""
Meme Engine Module.

This module provides a class for generating memes by adding text to images.

Dependencies:
    - PIL (Python Imaging Library)
    - random
    - os

Classes:
    - MemeEngine: A class for generating memes.

"""
from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine():
    """
    A class for generating memes by adding text to images.

    Attributes:
        out_dir (str): The output directory where the generated memes will be saved.

    Methods:
        make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
            Generates a meme by adding text to the image at the specified path and returns the path of the generated meme.

    """

    def __init__(self, out_dir: str):
        """Initialize a MemeEngine object."""
        self.out_dir = out_dir

    def resize_image(self, width):
        """Resize the image proportionally based on the specified width."""
        ratio = float(self.img.size[0]) / float(self.img.size[1])
        height = int(width / ratio)
        self.img = self.img.resize((width, height))

    def add_text(self, text, author):
        """Add text and author to the meme."""
        d = ImageDraw.Draw(self.img)

        quote_w = random.randint(
            18,
            int(self.img.size[0] / 8))

        quote_h = random.randint(
            20,
            self.img.size[1] - 100)

        font = ImageFont.truetype(
            "./src/_data/fonts/Futura-Heavy-font.ttf", 25
        )

        font1 = ImageFont.truetype(
            "./src/_data/fonts/Futura-Heavy-font.ttf", 20
        )

        d.text(
            (quote_w, quote_h),
            text,
            font=font,
            fill='white')

        d.text(
            (quote_w + 20, quote_h + 30),
            f'- {author}',
            font=font1,
            fill='white')

    def make_meme(
            self, img_path: str, text: str,
            author: str, width=500) -> str:
        """
        Generate a meme by adding text to the image at the specified path and return the path of the generated meme.

        Args:
            img_path (str): The path of the image to be used as the base for the meme.
            text (str): The text to be added to the image.
            author (str): The author of the quote.
            width (int): The desired width of the meme image (default is 500).

        Returns:
            str: The path of the generated meme.
        """
        self.img = Image.open(img_path)

        if self.img.size[0] > 500:
            self.resize_image(width)

        self.add_text(text, author)

        fname = f'{random.randint(0,100000)}.jpg'
        out_path = os.path.join(self.out_dir, fname)
        self.img.save(out_path)

        return(out_path)
