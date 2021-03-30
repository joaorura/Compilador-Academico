from identifiers.identifier import Identifier
from identifiers.finals.identifier_without_unknow import IDENTIFY_WITHOUT_UNKNOW
from tokens import UnknowToken

class UnknowIdentifier(Identifier):
    PATTERN = ''

    for i in IDENTIFY_WITHOUT_UNKNOW.values():
        PATTERN += f'({i.PATTERN})|'
    
    PATTERN = PATTERN[:-1]

    CATEGORY = UnknowToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> UnknowToken:
        if super().match(lexeme) == False:
            return UnknowToken(line, col, lexeme)
        else:
            return None
