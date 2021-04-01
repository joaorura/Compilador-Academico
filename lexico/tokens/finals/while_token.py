from tokens.token import Token


class WhileToken(Token):
    _ENUMERATION = 23
    CATEGORY = 'While'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
