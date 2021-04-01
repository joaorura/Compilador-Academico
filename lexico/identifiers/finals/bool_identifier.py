from identifiers.identifier import Identifier
from tokens import BoolToken


class BoolIdentifier(Identifier):
    PATTERN = r"True|False"

    CATEGORY = BoolToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> BoolToken:
        if super().match(lexeme):
            return BoolToken(line, col, lexeme)
        else:
            return None
