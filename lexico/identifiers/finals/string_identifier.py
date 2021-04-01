from identifiers.identifier import Identifier
from tokens import StringToken


class StringIdentifier(Identifier):
    PATTERN = r"\"[\w\s\[\]{}()<(>)\"'=|.,;!?]*\""

    CATEGORY = StringToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> StringToken:
        if super().match(lexeme):
            return StringToken(line, col, lexeme)
        else:
            return None
