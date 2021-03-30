from identifiers.identifier import Identifier
from identifiers.tipo_indentifier import TipoIndetifier
from identifiers.void_tipo_identifier import VoidTipoIdentifier
from identifiers.letra_maiscula_identifier import LetraMaiusculaIdentifier
from tokens import Token


IDENTIFY_ALL_FINALS = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier()
}


class IndetifierAll:
    def __init__(self):
        for i, j in IDENTIFY_ALL_FINALS.items():
            if type(i) != str:
                raise Exception()

            if(not issubclass(type(j), Identifier)):
                raise Exception

    def get_all_types(self):
        return list(IDENTIFY_ALL_FINALS.keys())

    def indentify(self, the_type: str, line: int, col: int, lexeme: str) -> Token:
        return IDENTIFY_ALL_FINALS[the_type].indentify(line, col, lexeme)

