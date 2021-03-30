from tokens.token import Token


class ElseToken(Token):
    _ENUMERATION = 12
    CATEGORY = 'Else'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
