from identifiers.identifier import Identifier
from tokens import MainToken


class MainIdentifier(Identifier):
    PATTERN = r'main'
    
    CATEGORY = MainToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> MainToken:
        if super().match(lexeme):
            return MainToken(line, col, lexeme)
        else:
            return None
