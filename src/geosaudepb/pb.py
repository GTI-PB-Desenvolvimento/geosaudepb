from abc import ABC, abstractmethod
from typing import List, Any

from .data import PBData


class _Base(ABC):
    @abstractmethod
    def get_all() -> List[Any]:
        pass

    @abstractmethod
    def get():
        pass


class Macroregiao(_Base):
    @staticmethod
    def get_all() -> List[str]:
        return list(PBData.data.keys())

    @staticmethod
    def get(macro) -> dict:
        return PBData.data[macro]
