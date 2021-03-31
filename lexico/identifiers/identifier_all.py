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
    def identify(the_type: str, line: int, col: int, lexeme: str) -> tuple:
        body = the_type[0].upper() + the_type.lower()[1:]
        result0 = IDENTIFY_ALL_FINALS[body].get_rest_token(lexeme)
        result1 = IDENTIFY_ALL_FINALS[body].get_token(lexeme)
        result2 = IDENTIFY_ALL_FINALS[body].identify(line, col, lexeme)

        if result1 is not None and result2 is not None:
            result2.set_lexeme(result1)

        return result0, result2

    def identify_all(self, line: int, col: int, lexeme: str) -> tuple:
        for i in self._types:
            rest_token, token_str, token_obj = self.identify(i, line, col, lexeme)

            if token_obj is not None:
                return rest_token, token_obj

        return '', self.identify(self._unknown, line, col, lexeme)
