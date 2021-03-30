from identifiers import IdentifierAll
from tokens import Token


class Read:
    def __init__(self, path):
        self._path = path
        self._file = open(path, 'r')
        self._identifiers_all = IdentifierAll()

        self._actual_col = None
        self._actual_line = 0
        self._max = None
        self._tokens = None

    def _read_next(self) -> str:
        line = self._file.readline()
        line = line.replace('\t', ' ')
        line = line.replace('\n', ' ')
        self._tokens = list(line.split(' '))
        self._tokens = filter(lambda x: x != '', self._tokens)
        self._actual_col = 0
        self._actual_line += 1
        self._max = len(self._tokens)

    def get_token(self) -> Token:
        if self._actual_line == self._actual_col:
            try:
                self._read_next()
            except StopIteration:
                return None

        actual_token = self._tokens[self._actual_col]
        self._actual_col += 1

        result = self._identifiers_all.identify_all(self._actual_line, self._actual_col, actual_token)

        if result is None:
            raise Exception
        else:
            return result
