from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TextIO


class Expression(ABC):
    @abstractmethod
    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        ...

    @abstractmethod
    def print_myself(self, output_stream: TextIO) -> None:
        ...


class ExpressionWithValue(ABC):
    @abstractmethod
    def get_value(self) -> int:
        ...
