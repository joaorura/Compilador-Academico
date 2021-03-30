from tokens.token import Token


class LetraMaiusculaToken(Token):
    _ENUMERATION = 3
    CATEGORY = 'LetraMaiuscula'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
