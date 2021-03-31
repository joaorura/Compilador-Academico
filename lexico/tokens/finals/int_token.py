from tokens.token import Token


class IntToken(Token):
    _ENUMERATION = 11
    CATEGORY = 'Int'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
