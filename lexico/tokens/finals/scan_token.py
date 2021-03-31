from tokens.token import Token


class ScanToken(Token):
    _ENUMERATION = 24
    CATEGORY = 'Scan'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
