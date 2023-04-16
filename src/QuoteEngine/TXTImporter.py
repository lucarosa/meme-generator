from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTImporter(IngestorInterface):
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest")

        quotes = []

        with open(path) as f:
            for line in f:
                parsed = line.strip().split("-")
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes
