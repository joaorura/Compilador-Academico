from identifiers.identifier import Identifier
from tokens import RetornoToken


class RetornoIdentifier(Identifier):
    PATTERN = r'return'
    
    CATEGORY = RetornoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> RetornoToken:
        if super().match(lexeme):
            return RetornoToken(line, col, lexeme)
        else:
            return None
