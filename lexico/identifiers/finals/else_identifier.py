from identifiers.identifier import Identifier
from tokens import ElseToken


class ElseIdentifier(Identifier):
    PATTERN = r'else'
    
    CATEGORY = ElseToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> ElseToken:
        if super().match(lexeme):
            return ElseToken(line, col, lexeme)
        else:
            return None
