from identifiers.identifier import Identifier
from tokens import OperadorMenorIgualToken


class OperadorMenorIgualIdentifier(Identifier):
    PATTERN = r"<="

    CATEGORY = OperadorMenorIgualToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorMenorIgualToken:
        if super().match(lexeme):
            return OperadorMenorIgualToken(line, col, lexeme)
        else:
            return None
