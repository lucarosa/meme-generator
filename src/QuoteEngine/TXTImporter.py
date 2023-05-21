from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTImporter(IngestorInterface):
    """
    A class for importing and parsing TXT files to extract quotes.

    Attributes:
        allowed_extension (List[str]): List of allowed file extensions for TXT files.

    Methods:
        parse(cls, path: str) -> List[QuoteModel]:
            Parses the TXT file at the specified path and returns a list of QuoteModel objects.

    """

    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from txt files."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest")

        quotes = []

        with open(path) as f:
            for line in f:
                parsed = line.strip().split("-")
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes
