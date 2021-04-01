from identifiers.identifier import Identifier
from tokens import ConstanteToken


class ConstanteIdentifier(Identifier):
    PATTERN = r'const'
    
    CATEGORY = ConstanteToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> ConstanteToken:
        if super().match(lexeme):
            return ConstanteToken(line, col, lexeme)
        else:
            return None
