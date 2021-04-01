from tokens.token import Token


class StringToken(Token):
    _ENUMERATION = 9
    CATEGORY = 'String'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
