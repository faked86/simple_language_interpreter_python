from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TextIO


class Expression(ABC):
    _tag: str

    @property
    def tag(self):
        return self._tag

    @abstractmethod
    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...


class ExpressionWithValueMixin(ABC):
    @abstractmethod
    def get_value(self) -> int:
        ...
