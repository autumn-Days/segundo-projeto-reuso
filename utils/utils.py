import subprocess as sp
import os
import resource
import time
import psutil #Essa biblioteca é para obter o tempo de cpu no windows. Tem que instalar ela.
from typing import List,Tuple
import multiprocessing as mp
import signal


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


#def contentReproducer(content:List[List[str]], _2print:bool,) -> None:


def __cpuTimer4Linux(command:List[str]) -> float:
    subProcess = sp.Popen(command)
    _, _, rusage = os.wait4(subProcess.pid, 0) #pid, status, rusage
    cpuTime = rusage.ru_utime + rusage.ru_stime
    return cpuTime


def __obtainOutput(command:List[str],getSignal=False) -> Tuple[str,str] | Tuple[str,str,str] :#retorna o output (stdout) e os erros (stderr)
    subProcess = sp.run(
        command,
        capture_output=True,
        text=True
    signal = ""
    if getSignal:
        sigRcvd = -subProcess.returncode
        signal = signal.Signals(sigRcvd).name
        return (subProcess.stdout, subProcess.stderr,signal)

    return (subProcess.stdout, subProcess.stderr)

def __cpuTimer4Windows(command:List[str]) -> float:
    subProcess = psutil.Popen(command)
    subProcess.wait()
    cpuTime = subProcess.cpu_times()
    cpuTime = cpuTime.user + cpuTime.system
    return cpuTime

def __realTimer(command:List[str]) -> float:
    start = time.time()
    sp.run(command)
    end =  time.time() - start
    return end

def cronometrarSubprocess(path:str, cmd:str, realTime:bool = True, captureOutput=False) -> float:
    command:List = []
    if cmd == "./":
        command = [f"./{path}"]
    else:
        command = [cmd,path]

    return __realTimer(command,captureOutput) if realTime else __cpuTimer4Linux(command,captureOutput)


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

def queue2List(queue:mp.Queue[Any],length) -> List[Any]:
    return [queue.get() for _ in range(length)]