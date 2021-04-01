from tokens.token import Token


class OperadorConcatenacaoToken(Token):
    _ENUMERATION = 26
    CATEGORY = 'OperadorConcatenacao'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
