from tokens.token import Token


class VerdadeiroToken(Token):
    _ENUMERATION = 13
    CATEGORY = 'Verdadeiro'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
