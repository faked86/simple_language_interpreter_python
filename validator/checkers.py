from abc import ABC, abstractclassmethod
from collections import deque

from validator.exceptions import CheckerError


class Checker(ABC):
    @abstractclassmethod
    def check(program_text: str):
        ...


class ParenthesesChecker(Checker):
    @classmethod
    def check(program_text: str):
        stack = deque()
        for index, char in enumerate(program_text):
            if char == "(":
                stack.append(index)
            if char == ")":
                try:
                    stack.pop()
                except IndexError:
                    raise CheckerError(f"Excess ')' bracket at {index}")
        if stack:
            raise CheckerError(f"Unclosed '(' bracket at {stack.pop()}")
