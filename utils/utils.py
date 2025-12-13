import subprocess as sp
import time
from typing import List

def prepareFileDestiny(origin:str, destiny:str, metricType) -> None:
    fileWithExtension:str = origin.split("/")[-1]
    fileName:str = fileWithExtension.split(".")[0]
    path:str = destiny + fileName + "." + metricType
    print(destiny, ',', fileName, ',', metricType)
    return path

def createFile(path:str,content:str) -> None:
    with open(f"{path}","w") as file:
        file.write(content)

def cronometrarSubprocess(path:str, cmd:str) -> float:
    command:List = []
    if cmd == "./":
        command = [f"./{cmd}"]
    else:
        command = [cmd,path]

    start = time.time()
    sp.run(command)
    end = time.time() - start

    return end

def prepareContent(totalTime):
    return f"segundos: {totalTime:.4f}\n"
