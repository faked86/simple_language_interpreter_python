from typing import TextIO

from models.expression import Expression
from models.value import Value


class Addition(Expression):
    def __init__(self, expr1: Expression, expr2: Expression) -> None:
        self.expression1 = expr1
        self.expression2 = expr2

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        res1 = self.expression1.evaluate(environment).get_value()
        res2 = self.expression2.evaluate(environment).get_value()
        return Value(res1 + res2)

    def print_myself(self, output_stream: TextIO) -> None:
        output_stream.write("(add ")
        self.expression1.print_myself(output_stream)
        output_stream.write(" ")
        self.expression2.print_myself(output_stream)
        output_stream.write(")")

    def get_value(self) -> int:
        return self.value


class Subtraction(Expression):
    def __init__(self, expr1: Expression, expr2: Expression) -> None:
        self.expression1 = expr1
        self.expression2 = expr2

    def evaluate(self, environment: dict[str, Expression]) -> Expression:
        res1 = self.expression1.evaluate(environment).get_value()
        res2 = self.expression2.evaluate(environment).get_value()
        return Value(res1 - res2)

    def print_myself(self, output_stream: TextIO) -> None:
        output_stream.write("(sub ")
        self.expression1.print_myself(output_stream)
        output_stream.write(" ")
        self.expression2.print_myself(output_stream)
        output_stream.write(")")

    def get_value(self) -> int:
        return self.value
