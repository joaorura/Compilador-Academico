from identifiers.finals.unknown_identifier import UnknowIdentifier
from identifiers.finals.tipo_indentifier import TipoIndetifier
from identifiers.finals.void_tipo_identifier import VoidTipoIdentifier
from identifiers.finals.letra_maiscula_identifier import LetraMaiusculaIdentifier
from identifiers.finals.letra_minuscula_identifier import LetraMinusculaIdentifier
from identifiers.finals.simbolos_identifier import SimboloIdentifier
from identifiers.finals.digitos_identifier import DigitosIdentifier
from identifiers.finals.underline_indetifier import UnderlineIdentifier
from identifiers.finals.constante_identifier import ConstanteIdentifier
from identifiers.finals.retorno_identifier import RetornoIdentifier

IDENTIFY_ALL_FINALS = {
    UnknowIdentifier.CATEGORY: UnknowIdentifier(),
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier(),
    LetraMinusculaIdentifier.CATEGORY: LetraMinusculaIdentifier(),
    SimboloIdentifier.CATEGORY: SimboloIdentifier(),
    DigitosIdentifier.CATEGORY: DigitosIdentifier(),
    UnderlineIdentifier.CATEGORY: UnderlineIdentifier()
    ConstanteIdentifier.CATEGORY: ConstanteIdentifier()
    RetornoIdentifier.CATEGORY: RetornoIdentifier()
}
