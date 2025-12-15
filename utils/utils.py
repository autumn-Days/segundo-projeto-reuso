import subprocess as sp
import os
import resource
import time
import psutil #Essa biblioteca é para obter o tempo de cpu no windows. Tem que instalar ela.
from typing import Any, List,Tuple, TYPE_CHECKING
import multiprocessing as mp
from utils.timerStrategy import TimerStrategy


if TYPE_CHECKING:
    QueueAny = mp.Queue[Any]
else:
    QueueAny = mp.Queue


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

def cronometrarSubprocess(path:str, cmd:str, timer:TimerStrategy) -> float:
    command:List = []
    if cmd == "./":
        command = [f"./{path}"]
    else:
        command = [cmd,path]

    return timer.measure(command)

def prepareContent(totalTime):
    return f"segundos: {totalTime:.4f}\n"

def initVariables(concurrent:bool, cpuTime:bool) -> Tuple[str,str]:
    execType = "concurrent" if concurrent else "sequential"
    metricType:str = ""

    if (cpuTime):
        metricType = "cpuTime"
    else:
        metricType = "realTime"
    return (execType,metricType)

def queue2List(queue:QueueAny,length) -> List[Any]:
    return [queue.get() for _ in range(length)]