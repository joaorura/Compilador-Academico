from tokens.token import Token


class LetraMinusculaToken(Token):
    _ENUMERATION = 4
    CATEGORY = 'LetraMinuscula'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
