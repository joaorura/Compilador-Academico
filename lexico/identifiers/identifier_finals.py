from identifiers.identifier import Identifier
from identifiers.tipo_indentifier import TipoIndetifier
from identifiers.void_tipo_identifier import VoidTipoIdentifier
from identifiers.letra_maiscula_identifier import LetraMaiusculaIdentifier
from identifiers.unknow_identifier import UnknowIdentifier


IDENTIFY_ALL_FINALS = {
    UnknowIdentifier.CATEGORY: UnknowIdentifier(),
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier()
}
