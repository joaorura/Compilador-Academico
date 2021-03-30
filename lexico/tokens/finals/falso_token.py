from tokens.token import Token


class FalsoToken(Token):
    _ENUMERATION = 14
    CATEGORY = 'Falso'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
