from tokens.token import Token


class ConstanteToken(Token):
    _ENUMERATION = 3
    CATEGORY = 'Constante'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
