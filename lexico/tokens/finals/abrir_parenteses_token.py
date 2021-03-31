from tokens.token import Token


class AbrirParentesesToken(Token):
    _ENUMERATION = 21
    CATEGORY = 'AbrirParenteses'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
