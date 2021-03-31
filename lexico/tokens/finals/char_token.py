from tokens.token import Token


class CharToken(Token):
    _ENUMERATION = 10
    CATEGORY = 'Char'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)