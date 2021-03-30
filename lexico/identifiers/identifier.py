import abc
import re

from tokens.token import Token

class Identifier(abc.ABC):
    def __init__(self, pattern: str):
        self._pattern = pattern

        self._regex = re.compile(self._pattern)

    def match(self, lexeme) -> bool:
        return bool(self._regex.fullmatch(lexeme))

    def get_pattern(self) -> str:
        return self._pattern

    @abc.abstractmethod
    def identify(self, line: int, col: int, lexeme: str) -> Token:
        pass
