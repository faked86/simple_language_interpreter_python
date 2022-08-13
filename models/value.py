from typing import TextIO

from models.expression import Expression


class Value(Expression):
    def __init__(self, value: int) -> None:
        self.value = value

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        return self

    def print_myself(self, output_stream: TextIO) -> None:
        output_stream.write(f"(val {self.value})")

    def get_value(self) -> int:
        return self.value
