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
from identifiers.finals.identificador_identifier import IdentificadorIdentifier
from identifiers.finals.operador_concatenacao_identifier import OperadorConcatenacaoIdentifier
from identifiers.finals.operador_ou_identifier import OperadorOuIdentifier
from identifiers.finals.operador_e_identifier import OperadorEIdentifier
from identifiers.finals.operador_maior_identifier import OperadorMaiorIdentifier
from identifiers.finals.operador_menor_identifier import OperadorMenorIdentifier
from identifiers.finals.operador_maior_igual_identifier import OperadorMaiorIgualIdentifier
from identifiers.finals.operador_menor_igual_identifier import OperadorMenorIgualIdentifier
from identifiers.finals.operador_igual_identifier import OperadorIgualIdentifier
from identifiers.finals.operador_adicao_identifier import OperadorAdicaoIdentifier
from identifiers.finals.operador_subtracao_identifier import OperadorSubtracaoIdentifier
from identifiers.finals.operador_multiplicacao_identifier import OperadorMultiplicacaoIdentifier
from identifiers.finals.operador_divisao_identifier import OperadorDivisaoIdentifier
from identifiers.finals.operador_resto_identifier import OperadorRestoIdentifier
from identifiers.finals.operador_negacao_identifier import OperadorNegacaoIdentifier
from identifiers.finals.for_identifier import ForIdentifier

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
    ForIdentifier.CATEGORY: ForIdentifier(),
    OperadorConcatenacaoIdentifier.CATEGORY: OperadorConcatenacaoIdentifier(),
    OperadorOuIdentifier.CATEGORY: OperadorOuIdentifier(),
    OperadorEIdentifier.CATEGORY: OperadorEIdentifier(),
    OperadorMaiorIgualIdentifier.CATEGORY: OperadorMaiorIgualIdentifier(),
    OperadorMenorIgualIdentifier.CATEGORY: OperadorMenorIgualIdentifier(),
    OperadorMaiorIdentifier.CATEGORY: OperadorMaiorIdentifier(),
    OperadorMenorIdentifier.CATEGORY: OperadorMenorIdentifier(),
    OperadorIgualIdentifier.CATEGORY: OperadorIgualIdentifier(),
    OperadorAdicaoIdentifier.CATEGORY: OperadorAdicaoIdentifier(),
    OperadorSubtracaoIdentifier.CATEGORY: OperadorSubtracaoIdentifier(),
    OperadorMultiplicacaoIdentifier.CATEGORY: OperadorMultiplicacaoIdentifier(),
    OperadorDivisaoIdentifier.CATEGORY: OperadorDivisaoIdentifier(),
    OperadorRestoIdentifier.CATEGORY: OperadorRestoIdentifier(),
    OperadorNegacaoIdentifier.CATEGORY: OperadorNegacaoIdentifier(),
    IdentificadorIdentifier.CATEGORY: IdentificadorIdentifier()
}
