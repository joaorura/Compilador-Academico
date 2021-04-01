from tokens.token import Token


class OperadorNegacaoToken(Token):
    _ENUMERATION = 39
    CATEGORY = 'OperadorNegacao'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
