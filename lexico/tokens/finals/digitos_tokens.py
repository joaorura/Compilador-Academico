from tokens.token import Token


class DigitosToken(Token):
    _ENUMERATION = 6
    CATEGORY = 'Digitos'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)

