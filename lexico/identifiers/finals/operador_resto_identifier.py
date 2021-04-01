from identifiers.identifier import Identifier
from tokens import OperadorRestoToken


class OperadorRestoIdentifier(Identifier):
    PATTERN = r"%"

    CATEGORY = OperadorRestoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorRestoToken:
        if super().match(lexeme):
            return OperadorRestoToken(line, col, lexeme)
        else:
            return None
