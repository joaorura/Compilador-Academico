import abc
import re

from tokens.token import Token


class Identifier(abc.ABC):
    def __init__(self, pattern: str):
        self._pattern = pattern
        self._regex = re.compile(self._pattern)

    def match(self, lexeme: str) -> bool:
        result = self._regex.sub('$%!', lexeme)
        result = result.split('$%!')

        if result[0] == '':
            self._rest_token = result[1]
            return bool(self._regex.match(lexeme))
        else:
            return False

    def get_token(self, lexeme) -> str:
        result = self._regex.sub('$%!', lexeme)
        result = result.split('$%!')

        if result[0] == '':
            return lexeme.replace(result[1], '')
        else:
            return None

    def get_rest_token(self, lexeme) -> str:
        result = self._regex.sub('$%!', lexeme)
        result = result.split('$%!')

        if result[0] == '':
            return result[1]
        else:
            return None

    def get_pattern(self) -> str:
        return self._pattern

    @abc.abstractmethod
    def identify(self, line: int, col: int, lexeme: str) -> Token:
        pass
