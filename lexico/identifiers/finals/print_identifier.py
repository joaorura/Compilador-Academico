from identifiers.identifier import Identifier
from tokens import PrintToken


class Printdentifier(Identifier):
    PATTERN = r'print'
    
    CATEGORY = PrintToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> PrintToken:
        if super().match(lexeme):
            return PrintToken(line, col, lexeme)
        else:
            return None
