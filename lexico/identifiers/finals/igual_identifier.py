from identifiers.identifier import Identifier
from tokens import IgualToken


class IgualIdentifier(Identifier):
    PATTERN = r"="

    CATEGORY = IgualToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> IgualToken:
        if super().match(lexeme):
            return IgualToken(line, col, lexeme)
        else:
            return None
