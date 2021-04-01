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

        self._read_next()

    def _read_next(self):
        line = self._file.readline()

        if len(line) == 0:
            raise StopIteration()

        print(f"{'{:02d}'.format(self._actual_line)}  ")

        line = line.replace('\t', ' ')
        line = line.replace('\n', ' ')
        self._tokens = list(line.split(' '))
        self._tokens = list(filter(lambda x: x != '', self._tokens))
        self._actual_col = 0
        self._actual_line += 1
        self._max = len(self._tokens)

    def get_token(self) -> Token:
        if self._actual_col >= self._max:
            try:
                self._read_next()

                while self._max == 0:
                    self._read_next()
            except StopIteration:
                return None

        actual_token = self._tokens[self._actual_col]

        rest, token = self._identifiers_all.identify_all(self._actual_line - 1, self._actual_col, actual_token)

        self._actual_col += 1

        if rest is None:
            return token
        elif rest != '':
            if self._actual_col >= self._max:
                self._tokens[self._actual_col - 1] = self._tokens[self._actual_col - 1].replace(rest, '')
                self._tokens.append('' + rest)
                self._max = len(self._tokens)
            else:
                self._tokens[self._actual_col - 1] = self._tokens[self._actual_col - 1].replace(rest, '')
                self._tokens[self._actual_col] = rest + self._tokens[self._actual_col]

        if token is None:
            raise Exception
        else:
            return token
