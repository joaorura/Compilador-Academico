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

    def get_all_types(self):
        return list(IDENTIFY_ALL_FINALS.keys())

    def indentify(self, the_type: str, line: int, col: int, lexeme: str) -> Token:
        return IDENTIFY_ALL_FINALS[the_type].identify(line, col, lexeme)

