from identifiers.identifier import Identifier
from tokens import OperadorIgualToken


class OperadorIgualIdentifier(Identifier):
    PATTERN = r'='
    
    CATEGORY = OperadorIgualToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorIgualToken:
        if super().match(lexeme):
            return OperadorIgualToken(line, col, lexeme)
        else:
            return None
