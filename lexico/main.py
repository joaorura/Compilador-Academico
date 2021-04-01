from identifiers import IdentifierAll
from read.read import Read
from sys import argv


FILE_TEST0 = '../programs_test/Hello World.txt'
FILE_TEST1 = '../programs_test/Fibonnaci.txt'
FILE_TEST2 = '../programs_test/ShellSort.txt'


def main():
    read = Read(argv[1])
    result = read.get_token()
    while result is not None:
        print(result)


def test():
    identifier_all = IdentifierAll()
    a, b = identifier_all.identify('Float', 0, 0, "21.0aaa")
    print(a)
    print(b)


def test_file():
    read = Read(FILE_TEST2)

    token = read.get_token()

    while token is not None:
        print(token)
        token = read.get_token()


if __name__ == '__main__':
    test()
