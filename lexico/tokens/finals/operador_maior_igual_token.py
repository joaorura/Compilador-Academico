from tokens.token import Token


class OperadorMaiorIgualToken(Token):
    _ENUMERATION = 31
    CATEGORY = 'OperadorMaiorIgual'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
