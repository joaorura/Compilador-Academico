from identifiers.identifier import Identifier
from tokens import CharToken


class CharIdentifier(Identifier):
    PATTERN = r"'[\w\s\[\]{}()<(>)\"'=|.,;]'"

    CATEGORY = CharToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> CharToken:
        if super().match(lexeme):
            return CharToken(line, col, lexeme)
        else:
            return None
