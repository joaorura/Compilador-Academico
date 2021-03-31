from identifiers.identifier import Identifier
from tokens import VerdadeiroToken


class VerdadeiroIdentifier(Identifier):
    PATTERN = r'True'
    
    CATEGORY = VerdadeiroToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> VerdadeiroToken:
        if super().match(lexeme):
            return VerdadeiroToken(line, col, lexeme)
        else:
            return None
