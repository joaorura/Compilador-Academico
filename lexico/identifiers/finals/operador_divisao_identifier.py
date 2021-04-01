from identifiers.identifier import Identifier
from tokens import OperadorDivisaoToken


class OperadorDivisaoIdentifier(Identifier):
    PATTERN = r'/'
    
    CATEGORY = OperadorDivisaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorDivisaoToken:
        if super().match(lexeme):
            return OperadorDivisaoToken(line, col, lexeme)
        else:
            return None
