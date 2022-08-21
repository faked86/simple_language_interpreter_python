from loguru import logger

from validator.checkers import Checker
from validator.exceptions import CheckerError, ValidationError


class Validator:
    def __init__(self, checkers: list[Checker]):
        self.checkers = checkers

    def validate(self, program: str):
        try:
            for checker in self.checkers:
                checker.check(program)
        except CheckerError as err:
            logger.error(err)
            raise ValidationError(err)
