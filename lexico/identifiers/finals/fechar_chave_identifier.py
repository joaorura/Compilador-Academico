from identifiers.identifier import Identifier
from tokens import FecharChaveToken


class FecharChaveIdentifier(Identifier):
    PATTERN = r"\]"

    CATEGORY = FecharChaveToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> FecharChaveToken:
        if super().match(lexeme):
            return FecharChaveToken(line, col, lexeme)
        else:
            return None
