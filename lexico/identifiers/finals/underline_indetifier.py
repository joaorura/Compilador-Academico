from identifiers.identifier import Identifier
from tokens import UnderlineToken


class UnderlineIdentifier(Identifier):
    PATTERN = r"_"

    CATEGORY = UnderlineToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> UnderlineToken:
        if super().match(lexeme):
            return UnderlineToken(line, col, lexeme)
        else:
            return None
