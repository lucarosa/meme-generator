from .IngestorInterface import IngestorInterface
import docx
from .QuoteModel import QuoteModel
from typing import List


class DocxImporter(IngestorInterface):
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
