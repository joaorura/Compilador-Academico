from identifiers.identifier import Identifier
from tokens import VoidTipoToken


class VoidTipoIdentifier(Identifier):
    _PATTERN = r'void'
    
    CATEGORY = VoidTipoToken.CATEGORY

    def __init__(self):
        super().__init__(self._PATTERN)

    def indentify(self, line: int, col: int, lexeme: str) -> VoidTipoToken:
        if super().match(lexeme) == True:
            return VoidTipoToken(line, col, lexeme)
        else:
            return None
