from tokens.token import Token


class OperadorMaiorToken(Token):
    _ENUMERATION = 29
    CATEGORY = 'OperadorMaior'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
