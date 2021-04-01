from tokens.token import Token


class ForToken(Token):
    _ENUMERATION = 25
    CATEGORY = 'For'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
