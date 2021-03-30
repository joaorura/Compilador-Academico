from identifiers.finals.tipo_indentifier import TipoIndetifier
from identifiers.finals.void_tipo_identifier import VoidTipoIdentifier
from identifiers.finals.letra_maiscula_identifier import LetraMaiusculaIdentifier
from identifiers.finals.letra_minuscula_identifier import LetraMinusculaIdentifier
from identifiers.finals.simbolos_identifier import SimboloIdentifier


IDENTIFY_WITHOUT_UNKNOW = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier(),
    LetraMinusculaIdentifier.CATEGORY: LetraMinusculaIdentifier(),
    SimboloIdentifier.CATEGORY: SimboloIdentifier(),
}