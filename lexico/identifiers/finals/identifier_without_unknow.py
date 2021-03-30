from identifiers.finals.tipo_indentifier import TipoIndetifier
from identifiers.finals.void_tipo_identifier import VoidTipoIdentifier
from identifiers.finals.letra_maiscula_identifier import LetraMaiusculaIdentifier
from identifiers.finals.letra_minuscula_identifier import LetraMinusculaIdentifier
from identifiers.finals.simbolos_identifier import SimboloIdentifier
from identifiers.finals.digitos_identifier import DigitosIdentifier
from identifiers.finals.underline_indetifier import UnderlineIdentifier


IDENTIFY_WITHOUT_UNKNOWN = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier(),
    LetraMinusculaIdentifier.CATEGORY: LetraMinusculaIdentifier(),
    SimboloIdentifier.CATEGORY: SimboloIdentifier(),
    DigitosIdentifier.CATEGORY: DigitosIdentifier(),
    UnderlineIdentifier.CATEGORY: UnderlineIdentifier()
}
