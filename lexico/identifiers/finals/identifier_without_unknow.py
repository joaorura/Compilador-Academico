from identifiers.finals.tipo_indentifier import TipoIndetifier
from identifiers.finals.void_tipo_identifier import VoidTipoIdentifier
from identifiers.finals.underline_indetifier import UnderlineIdentifier
from identifiers.finals.constante_identifier import ConstanteIdentifier
from identifiers.finals.main_identifier import MainIdentifier
from identifiers.finals.retorno_identifier import RetornoIdentifier
from identifiers.finals.if_identifier import IfIdentifier
from identifiers.finals.else_identifier import ElseIdentifier
from identifiers.finals.print_identifier import PrintIdentifier
from identifiers.finals.string_identifier import StringIdentifier
from identifiers.finals.char_identifier import CharIdentifier
from identifiers.finals.int_identifier import IntIdentifier
from identifiers.finals.float_identifier import FloatIdentifier
from identifiers.finals.bool_identifier import BoolIdentifier


IDENTIFY_WITHOUT_UNKNOWN = {
    TipoIndetifier.CATEGORY: TipoIndetifier(),
    VoidTipoIdentifier.CATEGORY: VoidTipoIdentifier(),
    UnderlineIdentifier.CATEGORY: UnderlineIdentifier(),
    ConstanteIdentifier.CATEGORY: ConstanteIdentifier(),
    MainIdentifier.CATEGORY: MainIdentifier(),
    RetornoIdentifier.CATEGORY: RetornoIdentifier(),
    IfIdentifier.CATEGORY: IfIdentifier(),
    ElseIdentifier.CATEGORY: ElseIdentifier(),
    PrintIdentifier.CATEGORY: PrintIdentifier(),
    StringIdentifier.CATEGORY: StringIdentifier(),
    CharIdentifier.CATEGORY: CharIdentifier(),
    IntIdentifier.CATEGORY: IntIdentifier(),
    FloatIdentifier.CATEGORY: FloatIdentifier(),
    BoolIdentifier.CATEGORY: BoolIdentifier(),
}
