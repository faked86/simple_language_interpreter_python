from typing import TextIO

from models.interfaces import Expression, ExpressionWithValue


class Value(Expression, ExpressionWithValue):
    def __init__(self, value: int) -> None:
        self.value = value

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        return self

    def print_myself(self, output_stream: TextIO) -> None:
        output_stream.write(f"(val {self.value})")

    def get_value(self) -> int:
        return self.value
