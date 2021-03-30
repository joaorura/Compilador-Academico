from identifiers.identifier import Identifier
from tokens import SimbolosToken


class SimboloIdentifier(Identifier):
    PATTERN = r"\[|\]|\{|\}|\(|\)|\<|\>|\"|\'|\=|\||\.|\,|\;"
    
    CATEGORY = SimbolosToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def indentify(self, line: int, col: int, lexeme: str) -> SimbolosToken:
        if super().match(lexeme) == True:
            return SimbolosToken(line, col, lexeme)
        else:
            return None
