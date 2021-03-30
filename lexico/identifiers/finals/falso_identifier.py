from identifiers.identifier import Identifier
from tokens import FalsoToken


class MainIdentifier(Identifier):
    PATTERN = r'False'
    
    CATEGORY = FalsoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> FalsoToken:
        if super().match(lexeme):
            return FalsoToken(line, col, lexeme)
        else:
            return None
