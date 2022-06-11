from os import path, listdir
from sys import argv
from typing import List, Set


def getAllFiles(directory: str) -> Set[str]:
    files = set()
    for file in listdir(directory):
        if file.endswith(".c") and path.isfile(path.join(directory, file)):
            files.add(path.join(directory, file))
    return files


def getFileName(args: List[str], directory: str) -> Set[str]:
    files = set()
    if "-all" in args:
        files = getAllFiles(directory)
    else:
        for element in args:
            if not element.startswith("-"):
                if element.startswith("/") and path.isfile(element):
                    files.add(element)

                elif path.isfile(path.join(directory, element)):
                    files.add(path.join(directory, element))
    return files


def main(args: List[str]) -> None:
    directory = path.dirname(path.abspath(__file__))
    files = getFileName(args, directory)
    functons = set()
    for file in files:
        pass
        


if __name__ == "__main__":
    print(getAllFiles("/home/dihellgo"))
