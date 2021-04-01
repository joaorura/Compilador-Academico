from tokens.token import Token


class IdentificadorToken(Token):
    _ENUMERATION = 40
    CATEGORY = 'Identificador'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
