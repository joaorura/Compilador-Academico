from tokens.token import Token


class AbrirColcheteToken(Token):
    _ENUMERATION = 20
    CATEGORY = 'AbrirColchete'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
