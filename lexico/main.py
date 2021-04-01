from read.read import Read
from sys import argv
import os
import pathlib


def get_path(path_abs: str):
    path = os.path.relpath(path_abs)

    if not os.path.isfile(path):
        print('O path passado não é um arquivo.')
        return None
    if pathlib.Path(path).suffix != '.d':
        print('Arquivo de formato errado.')
        return None

    return path


def main():
    print('Analisando arquivo: ', argv[1])

    path = get_path(argv[1])

    print('\n\n\n')

    read = Read(path)

    token = read.get_token()

    while token is not None:
        print(token)
        token = read.get_token()


if __name__ == '__main__':
    main()
