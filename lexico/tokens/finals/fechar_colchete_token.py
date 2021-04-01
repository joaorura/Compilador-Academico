from tokens.token import Token


class FecharColcheteToken(Token):
    _ENUMERATION = 21
    CATEGORY = 'FecharColchete'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
