from tokens.token import Token


class AbrirChaveToken(Token):
    _ENUMERATION = 17
    CATEGORY = 'AbrirChave'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
