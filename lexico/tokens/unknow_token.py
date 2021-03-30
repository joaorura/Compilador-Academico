from tokens.token import Token



class UnknowToken(Token):
    _ENUMERATION = 0
    CATEGORY = 'Desconhecido'
    
    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)    
