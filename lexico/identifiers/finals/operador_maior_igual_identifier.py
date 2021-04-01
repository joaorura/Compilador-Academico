from identifiers.identifier import Identifier
from tokens import OperadorMaiorIgualToken


class OperadorMaiorIgualIdentifier(Identifier):
    PATTERN = r">="

    CATEGORY = OperadorMaiorIgualToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorMaiorIgualToken:
        if super().match(lexeme):
            return OperadorMaiorIgualToken(line, col, lexeme)
        else:
            return None
