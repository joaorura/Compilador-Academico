from tokens.token import Token


class VoidTipoToken(Token):
    _ENUMERATION = 1
    CATEGORY = 'VoidTipo'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
