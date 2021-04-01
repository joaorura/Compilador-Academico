from identifiers.identifier import Identifier
from tokens import OperadorMultiplicacaoToken


class OperadorMultiplicacaoIdentifier(Identifier):
    PATTERN = r'*'
    
    CATEGORY = OperadorMultiplicacaoToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> OperadorMultiplicacaoToken:
        if super().match(lexeme):
            return OperadorMultiplicacaoToken(line, col, lexeme)
        else:
            return None
