from identifiers.identifier import Identifier
from tokens import DigitosToken


class DigitosIdentifier(Identifier):
    PATTERN = r"[0-9]"

    CATEGORY = DigitosToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> DigitosToken:
        if super().match(lexeme):
            return DigitosToken(line, col, lexeme)
        else:
            return None
