import re

from read import Read
from the_tokens import Token
from regex import REGEX


class Lexical:
    def __init__(self, path_file):
        self._path_file = path_file
        self._reader = Read(path_file)

    def _identify_lexeme(self) -> tuple:
        lexeme = self._reader.get_lexeme()

        if lexeme is None:
            return None

        for i, j in REGEX.items():
            search = re.search(f'^{j}', lexeme)
            if search is not None:
                rest_lexeme = re.sub(f'^{j}', '', lexeme)
                token = Token(self._reader.get_line(), self._reader.get_col(), search.group(0), i)

                return rest_lexeme, token

    def get_token(self) -> Token:
        result = self._identify_lexeme()
        if result is None:
            return None

        rest_lexeme, token = result

        self._reader.add_lexeme(rest_lexeme, token.get_lexeme())

        return token
