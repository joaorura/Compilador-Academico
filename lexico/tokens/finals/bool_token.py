from tokens.token import Token


class BoolToken(Token):
    _ENUMERATION = 13
    CATEGORY = 'Bool'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
