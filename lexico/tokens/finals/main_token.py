from tokens.token import Token


class MainToken(Token):
    _ENUMERATION = 9
    CATEGORY = 'Main'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
