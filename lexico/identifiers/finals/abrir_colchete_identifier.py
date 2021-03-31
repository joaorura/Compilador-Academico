from identifiers.identifier import Identifier
from tokens import AbrirColcheteToken


class AbrirColcheteIdentifier(Identifier):
    PATTERN = r"\[{"

    CATEGORY = AbrirColcheteToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> AbrirColcheteToken:
        if super().match(lexeme):
            return AbrirColcheteToken(line, col, lexeme)
        else:
            return None
