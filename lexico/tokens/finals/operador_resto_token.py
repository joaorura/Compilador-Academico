from tokens.token import Token


class OperadorRestoToken(Token):
    _ENUMERATION = 38
    CATEGORY = 'OperadorResto'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)