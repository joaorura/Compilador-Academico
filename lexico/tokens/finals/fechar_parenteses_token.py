from tokens.token import Token


class FecharParentesesToken(Token):
    _ENUMERATION = 22
    CATEGORY = 'FecharParenteses'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
