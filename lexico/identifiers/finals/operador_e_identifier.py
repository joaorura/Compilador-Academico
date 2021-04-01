from identifiers.identifier import Identifier
from tokens import OperadorEToken


class OperadorEIdentifier(Identifier):
    PATTERN = r"&&"

    CATEGORY = OperadorEToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorEToken:
        if super().match(lexeme):
            return OperadorEToken(line, col, lexeme)
        else:
            return None
