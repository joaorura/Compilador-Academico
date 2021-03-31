from identifiers.identifier import Identifier
from tokens import FecharParentesesToken


class FecharParentesesIdentifier(Identifier):
    PATTERN = r"\)"

    CATEGORY = FecharParentesesToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> FecharParentesesToken:
        if super().match(lexeme):
            return FecharParentesesToken(line, col, lexeme)
        else:
            return None
