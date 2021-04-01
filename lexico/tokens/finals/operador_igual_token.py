from tokens.token import Token


class OperadorIgualToken(Token):
    _ENUMERATION = 33
    CATEGORY = 'OperadorIgual'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
