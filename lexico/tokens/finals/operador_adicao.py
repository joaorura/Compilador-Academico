from tokens.token import Token


class OperadorAdicaoToken(Token):
    _ENUMERATION = 34
    CATEGORY = 'OperadorAdicao'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
