from identifiers.identifier import Identifier
from identifiers.finals.identifier_finals import IDENTIFY_ALL_FINALS
from tokens import Token


class IdentifierAll:
    def __init__(self):
        for i, j in IDENTIFY_ALL_FINALS.items():
            if type(i) != str:
                raise Exception()

            if(not issubclass(type(j), Identifier)):
                raise Exception

        self._all_types = list(IDENTIFY_ALL_FINALS.keys())
        self._unknown = self._all_types[0]
        self._types = self._all_types[1:]

    def get_all_types(self):
        return self._all_types

    @staticmethod
    def identify(the_type: str, line: int, col: int, lexeme: str) -> Token:
        body = the_type[0].upper() + the_type.lower()[1:]
        return IDENTIFY_ALL_FINALS[body].identify(line, col, lexeme)

    def identify_all(self, line: int, col: int, lexeme: str) -> Token:
        for i in self._types:
            result = self.identify(i, line, col, lexeme)

            if result is not None:
                return result

        return self.identify(self._unknown, line, col, lexeme)
