from tokens.token import Token


class UnderlineToken(Token):
    _ENUMERATION = 2
    CATEGORY = 'Underline'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)

