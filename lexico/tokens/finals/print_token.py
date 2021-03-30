from tokens.token import Token


class PrintToken(Token):
    _ENUMERATION = 15
    CATEGORY = 'Print'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
