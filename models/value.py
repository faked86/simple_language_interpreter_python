from typing import TextIO

from models.base_classes import Expression, ExpressionWithValueMixin


class Value(Expression, ExpressionWithValueMixin):
    _tag: str = "val"

    def __init__(self, value: int) -> None:
        self.value = value

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        return self

    def print_myself(self, output_stream: TextIO) -> None:
        output_stream.write(f"({self.tag} {self.value})")

    def get_value(self) -> int:
        return self.value
