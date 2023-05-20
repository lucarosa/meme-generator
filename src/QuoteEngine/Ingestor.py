from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Ingestor(IngestorInterface):
    """
    A class responsible for ingesting and parsing various file formats to extract quotes.

    Attributes:
        importers (List[Type[Importer]]): A list of supported importers for different file formats.

    Methods:
        parse(cls, path: str) -> List[QuoteModel]:
            Parses the given file at the specified path and returns a list of QuoteModel objects.
    """

    importers = [
        DocxImporter, CSVImporter,
        TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
