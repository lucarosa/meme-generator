from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random


class PDFImporter(IngestorInterface):
    """
    A class for importing and parsing PDF files to extract quotes.

    Attributes:
        allowed_extension (List[str]): List of allowed file extensions for PDF files.

    Methods:
        parse(cls, path: str) -> List[QuoteModel]:
            Parses the PDF file at the specified path and returns a list of QuoteModel objects.

    """

    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from pdf files."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest")

        quotes = []

        tmp = f'./src/tmp/{random.randint(0,100000)}.txt'
        call = subprocess.call(['pdftotext', "-layout", path, tmp])

        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    new_quote = QuoteModel(parsed[0], parsed[1])

                    quotes.append(new_quote)
        return quotes
