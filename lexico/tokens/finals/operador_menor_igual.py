from tokens.token import Token


class OperadorMenorIgualToken(Token):
    _ENUMERATION = 32
    CATEGORY = 'OperadorMenorIgual'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
