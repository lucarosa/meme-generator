from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVImporter(IngestorInterface):
    """
    A class for importing and parsing CSV files to extract quotes.

    Attributes:
        allowed_extension (List[str]): List of allowed file extensions for CSV files.

    Methods:
        parse(cls, path: str) -> List[QuoteModel]:
            Parses the CSV file at the specified path and returns a list of QuoteModel objects.

    """
    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest")

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])

            quotes.append(new_quote)

        return quotes
