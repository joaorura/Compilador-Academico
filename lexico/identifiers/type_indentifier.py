from identifiers.identifier import Identifier

from tokens.type_token import TypeToken
from tokens.unknow_token import UnknowToken


class TypeIndetifier(Identifier):
    _PATTERN = r'[A-Za-z]*'
    
    CATEGORY = TypeToken.CATEGORY

    def __init__(self):
        super().__init__(self._PATTERN)

    def indentify(self, line: int, col: int, lexeme: str) -> TypeToken:
        if super().match(lexeme) == True:
            return TypeToken(line, col, lexeme)
        else:
            return None
