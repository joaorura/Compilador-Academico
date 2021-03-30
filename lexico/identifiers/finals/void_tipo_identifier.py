from identifiers.identifier import Identifier
from tokens import VoidTipoToken


class VoidTipoIdentifier(Identifier):
    PATTERN = r'void'
    
    CATEGORY = VoidTipoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> VoidTipoToken:
        if super().match(lexeme) == True:
            return VoidTipoToken(line, col, lexeme)
        else:
            return None
