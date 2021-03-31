from identifiers.identifier import Identifier
from tokens import AbrirParentesesToken


class AbrirParentesesIdentifier(Identifier):
    PATTERN = r"\("

    CATEGORY = AbrirParentesesToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> AbrirParentesesToken:
        if super().match(lexeme):
            return AbrirParentesesToken(line, col, lexeme)
        else:
            return None
