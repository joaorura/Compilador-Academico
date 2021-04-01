from identifiers.identifier import Identifier
from tokens import OperadorNegacaoToken


class OperadorNegacaoIdentifier(Identifier):
    PATTERN = r"\!"

    CATEGORY = OperadorNegacaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorNegacaoToken:
        if super().match(lexeme):
            return OperadorNegacaoToken(line, col, lexeme)
        else:
            return None
