from tokens.token import Token


class FloatToken(Token):
    _ENUMERATION = 12
    CATEGORY = 'Float'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
