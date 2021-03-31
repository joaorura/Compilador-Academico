from identifiers.identifier import Identifier
from tokens import FloatToken


class FloatIdentifier(Identifier):
    PATTERN = r"\d+\.\d+"

    CATEGORY = FloatToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> FloatToken:
        if super().match(lexeme):
            return FloatToken(line, col, lexeme)
        else:
            return None
