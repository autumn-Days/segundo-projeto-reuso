import subprocess as sp
import time
from typing import List

def __createExtension(params:List[str]):
    execType, metricType = tuple(params)
    return f".{execType}_{metricType}"

def __createPath(destiny:str,fileName:str,params:List[str]):
    extension = __createExtension(params)
    path = destiny + "/" + fileName + extension
    return path

def __createFileName(origin:str):
    fileWithExtension:str = origin.split("/")[-1]
    fileName = fileWithExtension.split(".")[0]
    return fileName

def createDestinyPath(origin:str, destiny:str, params:List[str]) -> None:
    fileName = __createFileName(origin)
    extension = __createExtension(params)
    destinyPath:str = __createPath(destiny,fileName,params)
    #print(destiny, ',', fileName, ',', metricType) - não tem necessidade dessa parte
    return destinyPath

def createFile(path:str,content:str) -> None:
    with open(f"{path}","w") as file:
        file.write(content)

def cronometrarSubprocess(path:str, cmd:str) -> float:
    command:List = []
    if cmd == "./":
        command = [f"./{path}"]
    else:
        command = [cmd,path]

    start = time.time()
    sp.run(command)
    end = time.time() - start

    return end

def prepareContent(totalTime):
    return f"segundos: {totalTime:.4f}\n"
