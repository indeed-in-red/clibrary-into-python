from os import path, listdir
from sys import argv
from typing import List

def getAllFiles(directory:str) -> List[str]:
    files = []
    for file in listdir(directory):
        if file.endswith('.c') and path.isfile(path.join(directory, file)):
            files.append(path.join(directory, file))
    return files

def getFileName(args:List[str], directory:str) -> List[str]:
    files = []
    if '-all' in args:
        files = getAllFiles(directory)
    else:
        for element in args:
            if not element.startswith('-'):
                files.append(element)
    return files

def main(args:List[str]) -> None:
    directory = path.dirname(path.abspath(__file__))
    files = getFileName(args, directory)

if __name__ == '__main__':
    print(getAllFiles('/home/dihellgo'))