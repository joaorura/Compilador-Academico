from identifiers import IdentifierAll
from read.read import Read


FILE_TEST0 = '../programs_test/Hello_World.d'
FILE_TEST1 = '../programs_test/Fibonnaci.d'
FILE_TEST2 = '../programs_test/ShellSort.d'


def test():
    identifier_all = IdentifierAll()
    a, b = identifier_all.identify('Float', 0, 0, "21.0aaa")
    print(a)
    print(b)


def test_file():
    read = Read(FILE_TEST1)

    token = read.get_token()

    while token is not None:
        print(token)
        token = read.get_token()


if __name__ == '__main__':
    test_file()
