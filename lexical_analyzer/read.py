from os import path
from pathlib import Path
from re import match


class Read:
    def __init__(self, path_file: str):
        if Path(path_file).suffix != '.d' or \
                not path.isfile(path_file):
            raise Exception()

        path_file = path.relpath(path_file)
        self._reader = open(path_file, 'r')
        self._line = 0

        self._cols = None
        self._lexemes = None
        self._actual_lexeme = None
        self._max_cols = None

        self._read_line()

    def _separate_lexemes(self, line: str):
        line = line.replace('\n', '')
        self._lexemes = []
        lexeme = ''
        count = None
        for i, j in enumerate(line):
            if match(r'^(\t| )', j):
                if lexeme != '':
                    self._lexemes.append([count + 1, lexeme])
                    lexeme = ''
                    count = None
            else:
                if count is None:
                    count = i
                lexeme += j

        if lexeme != '':
            self._lexemes.append([count + 1, lexeme])

    def _read_line(self):
        result = self._reader.readline()

        if result == '':
            return False

        self._line += 1

        print(f'{"{:04d}  ".format(self._line)}')

        self._cols = 1
        self._actual_lexeme = 0
        self._max_cols = len(result)

        self._separate_lexemes(result)

        return True

    def _jump_white_line(self):
        while len(self._lexemes) == 0:
            test = self._read_line()

            if not test:
                return False

        return True

    def _check_end_line(self):
        if self._actual_lexeme == len(self._lexemes):
            return self._read_line()

        return True

    def get_line(self) -> int:
        return self._line

    def get_col(self):
        return self._cols

    def add_lexeme(self, rest_token: str, lexeme: str):
        if rest_token == '':
            return

        if self._actual_lexeme >= len(self._lexemes):
            the = self._lexemes[self._actual_lexeme - 1]
            the[1] = lexeme
            col = the[0] + len(the[1]) + 1
            self._lexemes.append([col, rest_token])
        else:
            the = self._lexemes[self._actual_lexeme]
            self._lexemes[self._actual_lexeme - 1][1] = lexeme
            the[1] = rest_token + the[1]
            the[0] -= len(rest_token)

    def get_lexeme(self) -> str:
        if not self._check_end_line() or not self._jump_white_line():
            return None

        col, lexeme = self._lexemes[self._actual_lexeme]
        self._cols = col
        self._actual_lexeme += 1

        return lexeme

