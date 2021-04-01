from identifiers.identifier import Identifier
from tokens import OperadorSubtracaoToken


class OperadorSubtracaoIdentifier(Identifier):
    PATTERN = r'-'
    
    CATEGORY = OperadorSubtracaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorSubtracaoToken:
        if super().match(lexeme):
            return OperadorSubtracaoToken(line, col, lexeme)
        else:
            return None
