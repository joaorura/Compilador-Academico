from identifiers.identifier import Identifier
from tokens import IdentificadorToken


class IdentificadorIdentifier(Identifier):
    PATTERN = r"_{0,1}[A-Za-z0-9_]+(\[\d*\])*"

    CATEGORY = IdentificadorToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> IdentificadorToken:
        if super().match(lexeme):
            return IdentificadorToken(line, col, lexeme)
        else:
            return None
