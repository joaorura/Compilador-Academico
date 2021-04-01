from identifiers.identifier import Identifier
from tokens import IfToken


class IfIdentifier(Identifier):
    PATTERN = r'if'
    
    CATEGORY = IfToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> IfToken:
        if super().match(lexeme):
            return IfToken(line, col, lexeme)
        else:
            return None
