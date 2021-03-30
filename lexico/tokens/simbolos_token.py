from tokens.token import Token


class SimbolosToken(Token):
    _ENUMERATION = 5
    CATEGORY = 'Simbolos'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
