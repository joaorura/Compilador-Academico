from tokens.token import Token


class OperadorEToken(Token):
    _ENUMERATION = 28
    CATEGORY = 'OperadorE'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
