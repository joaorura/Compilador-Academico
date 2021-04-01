from tokens.token import Token


class OperadorOuToken(Token):
    _ENUMERATION = 27
    CATEGORY = 'OperadorOu'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
