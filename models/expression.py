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

    def set_own_environment(self, environment: dict[str, Expression]) -> None:
        return

    def get_value(self) -> int:
        raise NotImplementedError(f"{type(self)} is a bad class to call get_value.")

    def get_id(self) -> str:
        raise NotImplementedError(f"{type(self)} is a bad class to call get_id.")

    def get_body(self) -> Expression:
        raise NotImplementedError(f"{type(self)} is a bad class to call get_body.")

    def get_own_environment(self) -> dict[str, Expression]:
        raise NotImplementedError(
            f"{type(self)} is a bad class to call get_own_environment."
        )
