from identifiers.identifier import Identifier
from tokens import OperadorMenorToken


class OperadorMenorIdentifier(Identifier):
    PATTERN = r"<"

    CATEGORY = OperadorMenorToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorMenorToken:
        if super().match(lexeme):
            return OperadorMenorToken(line, col, lexeme)
        else:
            return None
