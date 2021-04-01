from identifiers.identifier import Identifier
from tokens import WhileToken


class WhileIdentifier(Identifier):
    PATTERN = r"while"

    CATEGORY = WhileToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> WhileToken:
        if super().match(lexeme):
            return WhileToken(line, col, lexeme)
        else:
            return None
