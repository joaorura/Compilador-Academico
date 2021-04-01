from identifiers.identifier import Identifier
from tokens import AbrirChaveToken


class AbrirChaveIdentifier(Identifier):
    PATTERN = r"\["

    CATEGORY = AbrirChaveToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> AbrirChaveToken:
        if super().match(lexeme):
            return AbrirChaveToken(line, col, lexeme)
        else:
            return None
