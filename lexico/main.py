from identifiers import IdentifierAll
from read.read import Read
from sys import argv


def main():
    read = Read(argv[1])
    result = read.get_token()
    while result is not None:
        print(result)


def test():
    identifier_all = IdentifierAll()
    print(identifier_all.identify('Underline', 0, 0, "_"))


if __name__ == '__main__':
    test()
