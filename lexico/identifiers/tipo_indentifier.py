from identifiers.identifier import Identifier
from tokens import TipoToken


class TipoIndetifier(Identifier):
    _PATTERN = r'(bool)|(char)|(int)|(float)|(char)|(string)'
    
    CATEGORY = TipoToken.CATEGORY

    def __init__(self):
        super().__init__(self._PATTERN)

    def indentify(self, line: int, col: int, lexeme: str) -> TipoToken:
        if super().match(lexeme) == True:
            return TipoToken(line, col, lexeme)
        else:
            return None
