from identifiers.identifier import Identifier
from tokens import LetraMinusculaToken


class LetraMinusculaIdentifier(Identifier):
    PATTERN = r'[a-z]'
    
    CATEGORY = LetraMinusculaToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> LetraMinusculaToken:
        if super().match(lexeme):
            return LetraMinusculaToken(line, col, lexeme)
        else:
            return None
