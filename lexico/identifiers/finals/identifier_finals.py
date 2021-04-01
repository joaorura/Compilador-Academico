from identifiers.finals.unknown_identifier import UnknowIdentifier
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
from identifiers.finals.igual_identifier import IgualIdentifier
from identifiers.finals.virgula_identifier import VirgulaIdentifier
from identifiers.finals.ponto_virgula_identifier import PontoVirgulaIdentifier
from identifiers.finals.abrir_chave_identifier import AbrirChaveIdentifier
from identifiers.finals.fechar_chave_identifier import FecharChaveIdentifier
from identifiers.finals.abrir_colchete_identifier import AbrirColcheteIdentifier
from identifiers.finals.fechar_colchete_identifier import FecharColcheteIdentifier
from identifiers.finals.abrir_parenteses_identifier import AbrirParentesesIdentifier
from identifiers.finals.fechar_parenteses_identifier import FecharParentesesIdentifier
from identifiers.finals.while_identifier import WhileIdentifier
from identifiers.finals.scan_identifier import ScanIdentifier

IDENTIFY_ALL_FINALS = {
    UnknowIdentifier.CATEGORY: UnknowIdentifier(),
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
    IgualIdentifier.CATEGORY: IgualIdentifier(),
    VirgulaIdentifier.CATEGORY: VirgulaIdentifier(),
    PontoVirgulaIdentifier.CATEGORY: PontoVirgulaIdentifier(),
    AbrirChaveIdentifier.CATEGORY: AbrirChaveIdentifier(),
    FecharChaveIdentifier.CATEGORY: FecharChaveIdentifier(),
    AbrirColcheteIdentifier.CATEGORY: AbrirColcheteIdentifier(),
    FecharColcheteIdentifier.CATEGORY: FecharColcheteIdentifier(),
    AbrirParentesesIdentifier.CATEGORY: AbrirParentesesIdentifier(),
    FecharParentesesIdentifier.CATEGORY: FecharParentesesIdentifier(),
    WhileIdentifier.CATEGORY: WhileIdentifier(),
    ScanIdentifier.CATEGORY: ScanIdentifier(),
}
