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
        """
        Initializes a MemeEngine object.

        Args:
            out_dir (str): The output directory where the generated memes will be saved.

        """
        self.out_dir = out_dir

    def make_meme(
            self, img_path: str, text: str,
            author: str, width=500) -> str:

        img = Image.open(img_path)

        if img.size[0] > 500:
            ratio = float(img.size[0]) / float(img.size[1])
            height = int(width / ratio)
            img = img.resize((width, height))

        d = ImageDraw.Draw(img)

        quote_w = random.randint(20, img.size[0] / 4)
        quote_h = random.randint(20, img.size[1] - 100)
        font = ImageFont.truetype("./_data/fonts/Futura-Heavy-font.ttf", 25)
        font1 = ImageFont.truetype("./_data/fonts/Futura-Heavy-font.ttf", 20)
        d.text((quote_w, quote_h), text, font=font, fill='white')
        d.text((quote_w + 20, quote_h + 30), f'- {author}', font=font1, fill='white')

        fname = f'{random.randint(0,100000)}.jpg'
        out_path = os.path.join(self.out_dir, fname)
        img.save(out_path)

        return(out_path)
