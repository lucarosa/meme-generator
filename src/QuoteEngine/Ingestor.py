from .IngestorInterface import IngestorInterface
from typing import List
# import docx
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Ingestor(IngestorInterface):
    importers = [
        DocxImporter, CSVImporter,
        TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
