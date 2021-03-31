from tokens.token import Token


class PontoVirgulaToken(Token):
    _ENUMERATION = 16
    CATEGORY = 'PontoVirgula'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
