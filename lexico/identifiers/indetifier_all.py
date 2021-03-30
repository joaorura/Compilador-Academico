from identifiers.identifier import Identifier
from identifiers.tipo_indentifier import TipoIndetifier
from identifiers.void_tipo_identifier import VoidTipoIdentifier
from tokens import Token

_IDENTIFY_ALL = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier()
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

