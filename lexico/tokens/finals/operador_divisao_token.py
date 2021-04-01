from tokens.token import Token


class OperadorDivisaoToken(Token):
    _ENUMERATION = 37
    CATEGORY = 'OperadorDivisao'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)