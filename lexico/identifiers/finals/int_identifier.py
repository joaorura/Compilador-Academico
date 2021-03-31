from identifiers.identifier import Identifier
from tokens import IntToken


class IntIdentifier(Identifier):
    PATTERN = r"\d+"

    CATEGORY = IntToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> IntToken:
        if super().match(lexeme):
            return IntToken(line, col, lexeme)
        else:
            return None
