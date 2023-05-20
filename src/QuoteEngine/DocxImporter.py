from .IngestorInterface import IngestorInterface
import docx
from .QuoteModel import QuoteModel
from typing import List


class DocxImporter(IngestorInterface):
    """
    A class for importing and parsing Docx files to extract quotes.

    Attributes:
        allowed_extension (List[str]): List of allowed file extensions for Docx files.

    Methods:
        parse(cls, path: str) -> List[QuoteModel]:
            Parses the Docx file at the specified path and returns a list of QuoteModel objects.

    """
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                new_quote = QuoteModel(str(parsed[0]), str(parsed[1]))
                quotes.append(new_quote)

        return quotes
