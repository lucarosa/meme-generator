from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
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
