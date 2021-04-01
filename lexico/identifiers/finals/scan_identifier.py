from identifiers.identifier import Identifier
from tokens import ScanToken


class ScanIdentifier(Identifier):
    PATTERN = r"scan"

    CATEGORY = ScanToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> ScanToken:
        if super().match(lexeme):
            return ScanToken(line, col, lexeme)
        else:
            return None
