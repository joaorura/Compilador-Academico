from identifiers.identifier import Identifier
from tokens import OperadorAdicaoToken


class OperadorAdicaoIdentifier(Identifier):
    PATTERN = r'+'
    
    CATEGORY = OperadorAdicaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorAdicaoToken:
        if super().match(lexeme):
            return OperadorAdicaoToken(line, col, lexeme)
        else:
            return None
