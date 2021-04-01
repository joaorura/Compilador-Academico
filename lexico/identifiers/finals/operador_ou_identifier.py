from identifiers.identifier import Identifier
from tokens import OperadorOuToken


class OperadorOuIdentifier(Identifier):
    PATTERN = r"\||"

    CATEGORY = OperadorOuToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorOuToken:
        if super().match(lexeme):
            return OperadorOuToken(line, col, lexeme)
        else:
            return None
