from identifiers.identifier import Identifier
from tokens import LetraMaiusculaToken


class LetraMaiusculaIdentifier(Identifier):
    _PATTERN = r'[A-Z]'
    
    CATEGORY = LetraMaiusculaToken.CATEGORY

    def __init__(self):
        super().__init__(self._PATTERN)

    def indentify(self, line: int, col: int, lexeme: str) -> LetraMaiusculaToken:
        if super().match(lexeme) == True:
            return LetraMaiusculaToken(line, col, lexeme)
        else:
            return None
