from identifiers.identifier import Identifier
from tokens import OperadorConcatenacaoToken


class FloatIdentifier(Identifier):
    PATTERN = r"::"

    CATEGORY = OperadorConcatenacaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorConcatenacaoToken:
        if super().match(lexeme):
            return OperadorConcatenacaoToken(line, col, lexeme)
        else:
            return None
