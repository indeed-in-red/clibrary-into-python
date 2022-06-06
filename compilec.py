from os import path
from sys import argv
from typing import List

def main(args:List[str]) -> None:
    directory = path.dirname(path.abspath(__file__))
    print(directory)
    #file = getFileName(args)

if __name__ == '__main__':
    main(argv)