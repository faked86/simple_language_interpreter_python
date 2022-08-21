from typing import TextIO

from models.base_classes import Expression, ExpressionWithValueMixin


class Value(Expression, ExpressionWithValueMixin):
    _tag: str = "val"

    def __init__(self, value: int | float) -> None:
        self.value = value

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        return self

    def __str__(self) -> str:
        return f"({self.tag} {self.value})"

    def get_value(self) -> int | float:
        return self.value
