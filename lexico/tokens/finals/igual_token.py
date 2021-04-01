from tokens.token import Token


class IgualToken(Token):
    _ENUMERATION = 14
    CATEGORY = 'Igual'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
