from identifiers.identifier import Identifier
from tokens import FecharColcheteToken


class FecharColcheteIdentifier(Identifier):
    PATTERN = r"\}"

    CATEGORY = FecharColcheteToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> FecharColcheteToken:
        if super().match(lexeme):
            return FecharColcheteToken(line, col, lexeme)
        else:
            return None
