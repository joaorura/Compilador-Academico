from tokens.token import Token


class OperadorMultiplicacaoToken(Token):
    _ENUMERATION = 36
    CATEGORY = 'OperadorMultiplicacao'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
