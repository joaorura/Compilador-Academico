from identifiers.identifier import Identifier
from tokens import PontoVirgulaToken


class PontoVirgulaIdentifier(Identifier):
    PATTERN = r";"

    CATEGORY = PontoVirgulaToken.CATEGORY

    def __init__(self):
        super().__init__(self.PATTERN)

    def identify(self, line: int, col: int, lexeme: str) -> PontoVirgulaToken:
        if super().match(lexeme):
            return PontoVirgulaToken(line, col, lexeme)
        else:
            return None
