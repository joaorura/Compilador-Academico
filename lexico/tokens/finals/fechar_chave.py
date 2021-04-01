from tokens.token import Token


class FecharChaveToken(Token):
    _ENUMERATION = 18
    CATEGORY = 'FecharChave'

    def __init__(self, line: int, col: int, lexeme: str):
        super().__init__(line, col, self._ENUMERATION, self.CATEGORY, lexeme)
