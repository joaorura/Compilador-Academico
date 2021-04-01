from tokens.token import Token


class OperadorMenorToken(Token):
    _ENUMERATION = 30
    CATEGORY = 'OperadorMenor'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
