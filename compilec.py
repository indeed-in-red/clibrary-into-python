from os import path
from sys import argv
from typing import List

def getAllFiles(directory:str) -> List[str]:
    
    return files

def getFileName(args:List[str]) -> List[str]:
    files = []
    if '-all' in args:
        files = getAllFiles(directory)
    for element in args:
        if not element.startswith('-'):
            files.append(element)
    return files

def main(args:List[str]) -> None:
    directory = path.dirname(path.abspath(__file__))
    files = getFileName(args, directory)

if __name__ == '__main__':
    print(getAllFiles('/home/dihellgo'))