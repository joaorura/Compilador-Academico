from identifiers.identifier import Identifier
from identifiers.type_indentifier import TypeIndetifier

from tokens.token import Token

_IDENTIFY_ALL = {
    TypeIndetifier.CATEGORY: TypeIndetifier()
}


class IndetifierAll:
    def __init__(self):
        for i, j in _IDENTIFY_ALL.items():
            if type(i) != str:
                raise Exception()

            if(not issubclass(type(j), Identifier)):
                raise Exception

    def get_all_types(self):
        return list(_IDENTIFY_ALL.keys())

    def indentify(self, the_type: str, line: int, col: int, lexeme: str) -> Token:
        return _IDENTIFY_ALL[the_type].indentify(line, col, lexeme)

