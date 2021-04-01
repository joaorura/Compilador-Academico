from identifiers.identifier import Identifier
from tokens import OperadorNegacaoToken


class OperadorNegacaoIdentifier(Identifier):
    PATTERN = r"_{0,1}[A-Za-z0-9_]+(\[\d*\])*"

    CATEGORY = OperadorNegacaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorNegacaoToken:
        if super().match(lexeme):
            return OperadorNegacaoToken(line, col, lexeme)
        else:
            return None
