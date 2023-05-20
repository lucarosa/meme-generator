from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    An abstract base class representing an interface for file ingestors.

    Attributes:
        allowed_extension (List[str]): List of allowed file extensions for the ingestor.

    Methods:
        can_ingest(cls, path: str) -> bool:
            Checks if the ingestor can ingest a file with the given path.

        parse(cls, path: str) -> List[QuoteModel]:
            Abstract method to be implemented by subclasses for parsing a file and returning a list of QuoteModel objects.

    """
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split(".")[-1]
        # print(f'the extension is {ext}')
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
