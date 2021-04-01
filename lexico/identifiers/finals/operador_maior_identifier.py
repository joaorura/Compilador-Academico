from identifiers.identifier import Identifier
from tokens import OperadorMaiorToken


class OperadorMaiorIdentifier(Identifier):
    PATTERN = r">"

    CATEGORY = OperadorMaiorToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorMaiorToken:
        if super().match(lexeme):
            return OperadorMaiorToken(line, col, lexeme)
        else:
            return None
