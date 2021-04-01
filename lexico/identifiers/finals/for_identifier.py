from identifiers.identifier import Identifier
from tokens import ForToken


class ForIdentifier(Identifier):
    PATTERN = r"for"

    CATEGORY = ForToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> ForToken:
        if super().match(lexeme):
            return ForToken(line, col, lexeme)
        else:
            return None
