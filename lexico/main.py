from identifiers import IdentifierAll
from read.read import Read
from sys import argv


FILE_TEST = 'C:\\Users\\jmess\\Downloads\\main.txt'


def main():
    read = Read(argv[1])
    result = read.get_token()
    while result is not None:
        print(result)


def test():
    identifier_all = IdentifierAll()
    a, b = identifier_all.identify('float', 0, 0, "21.0aaa")
    print(a)
    print(b)


def test_file():
    read = Read(FILE_TEST)

    token = read.get_token()

    while token is not None:
        print(token)
        token = read.get_token()


if __name__ == '__main__':
    test_file()
