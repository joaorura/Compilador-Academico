from identifiers.finals.tipo_indentifier import TipoIndetifier
from identifiers.finals.void_tipo_identifier import VoidTipoIdentifier
from identifiers.finals.letra_maiscula_identifier import LetraMaiusculaIdentifier
from identifiers.finals.letra_minuscula_identifier import LetraMinusculaIdentifier
from identifiers.finals.simbolos_identifier import SimboloIdentifier
from identifiers.finals.digitos_identifier import DigitosIdentifier
from identifiers.finals.underline_indetifier import UnderlineIdentifier
from identifiers.finals.constante_identifier import ConstanteIdentifier
from identifiers.finals.main_identifier import MainIdentifier
from identifiers.finals.retorno_identifier import RetornoIdentifier
from identifiers.finals.if_identifier import IfIdentifier
from identifiers.finals.else_identifier import ElseIdentifier
from identifiers.finals.verdadeiro_identifier import VerdadeiroIdentifier
from identifiers.finals.falso_identifier import FalsoIdentifier
from identifiers.finals.print_identifier import PrintIdentifier


IDENTIFY_WITHOUT_UNKNOWN = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    LetraMaiusculaIdentifier.CATEGORY: LetraMaiusculaIdentifier(),
    LetraMinusculaIdentifier.CATEGORY: LetraMinusculaIdentifier(),
    SimboloIdentifier.CATEGORY: SimboloIdentifier(),
    DigitosIdentifier.CATEGORY: DigitosIdentifier(),
    UnderlineIdentifier.CATEGORY: UnderlineIdentifier(),
    ConstanteIdentifier.CATEGORY: ConstanteIdentifier(),
    MainIdentifier.CATEGORY: MainIdentifier(),
    RetornoIdentifier.CATEGORY: RetornoIdentifier(),
    IfIdentifier.CATEGORY: IfIdentifier(),
    ElseIdentifier.CATEGORY: ElseIdentifier(),
    VerdadeiroIdentifier.CATEGORY: VerdadeiroIdentifier(),
    FalsoIdentifier.CATEGORY: FalsoIdentifier(),
    PrintIdentifier.CATEGORY: PrintIdentifier(),
}
