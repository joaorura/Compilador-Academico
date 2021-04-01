from identifiers.identifier import Identifier
from tokens import VirgulaToken


class VirgulaIdentifier(Identifier):
    PATTERN = r"\,"

    CATEGORY = VirgulaToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> VirgulaToken:
        if super().match(lexeme):
            return VirgulaToken(line, col, lexeme)
        else:
            return None
