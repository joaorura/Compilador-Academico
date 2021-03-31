import abc

class Token(abc.ABC):
    def __init__(self, line: int, col: int, enumeration: int, category: str, lexeme: str):
        self._line = line
        self._col = col

        self._enumeration = enumeration
        self._category = category
        
        self._lexeme = lexeme

    def get_line(self) -> int:
        return self._line

    def get_col(self) -> int:
        return self._col

    def get_enumeration(self) -> int:
        return self._enumeration

    def get_category(self) -> str:
        return self._category

    def get_lexeme(self) -> str:
        return self._lexeme

    def set_lexeme(self, lexeme: str):
        self._lexeme = lexeme

    def __str__(self) -> str:
        return f'          [{self._line}, {self._col}] ({self._enumeration}, {self._category}) [{self._lexeme}]'
