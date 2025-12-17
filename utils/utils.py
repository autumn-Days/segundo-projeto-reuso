import subprocess as sp
import os
import resource
import time
import psutil #Essa biblioteca é para obter o tempo de cpu no windows. Tem que instalar ela.
from typing import List,Tuple,Any
import multiprocessing as mp
import signal

#INÍCIO: funções de Reprodutor
def __createSuffix(params:List[str]):
    #modificado
    #ok
    """
    execType: parallel, sequential
    metricType: cpu_time, real_time
    output
    signal
    [(valor|None),(valor1|valor2|None),(valor|None),(valor|None)]
    """
    suffix = ""

    for param in params:
        if param != None:
            suffix += f"_{param}"
    return f"{suffix}.dat"
def __createPath(destiny:str,fileName:str,params:List[str]):
    #ok
    extension = __createSuffix(params)
    path = destiny + "/" + fileName + extension
    return path
def __createFileName(origin:str):
    #ok
    fileWithExtension:str = origin.split("/")[-1]
    fileName = fileWithExtension.split(".")[0]
    return fileName

def createDestinyPath(origin:str, destiny:str, params:List[str]) -> None:
    #ok
    fileName = __createFileName(origin)
    extension = __createSuffix(params)
    destinyPath:str = __createPath(destiny,fileName,params)
    return destinyPath

def createFile(path:str,content:str) -> None:
    #ok
    with open(f"{path}","w") as file:
        file.write(content)
def prepareContent(totalTime:float=None, output:Tuple[str,str]=None, signal:str=None) -> str:
    #ok
    #modificado
    content = ""
    if totalTime:
        content += f"segundos:\n\t{totalTime:.5f}\n" 
    if output != (None,None):
        stdout = output[0]
        stderr = output[1]
        content += f"stdout:\n\n{stdout}\n\n"
        content += f"stderr:\n\n{stderr}\n\n"
    if signal:
        content += f"signal:\n\t{signal}\n"
    return 

def imprimirTempo()
#FIM: funções de Reprodutor


#Início: Executor
def __makeCommand(path:str,cmd:str) -> List[str]:
    #ok
    command:List = []
    if cmd == "./":
        command = [f"./{path}"]
    else:
        command = [cmd,path]
    return command
def __realTimer(command:List[str]) -> float:
    #ok
    start = time.time()
    sp.run(
        command,
        stdout=sp.PIPE
        stderr=sp.PIPE,
        )
    end =  time.time() - start
    return end
def __cpuTimer4Linux(command:List[str]) -> float:
    #ok
    subProcess = sp.Popen(
        command
        stdout=sp.PIPE
        sterr=sp.PIPE)
    _, _, rusage = os.wait4(subProcess.pid, 0) #pid, status, rusage
    cpuTime = rusage.ru_utime + rusage.ru_stime
    return cpuTime
def __cpuTimer4Windows(command:List[str]) -> float:
    #vou tirar depois
    subProcess = psutil.Popen(command)
    subProcess.wait()
    cpuTime = subProcess.cpu_times()
    cpuTime = cpuTime.user + cpuTime.system
    return cpuTime
def __obtainOutput(command:List[str],captureOutput=False,captureSignal=False) -> Any : # ((str,str,str),(str,str),str
    #ok
    subProcess = sp.run(
        command,
        capture_output=True,
        text=True)
    _signal = None
    if subProcess.returncode < 0 :
        sigRcvd = -subProcess.returncode
        _signal = signal.Signals(sigRcvd).name #só da para mapear em um nome se o código for negativo
    _signal = str(subProcess.returncode)
    if captureOutput and captureSignal:
        return (subProcess.stdout, subProcess.stderr,_signal)
    elif captureOutput:
        return (subProcess.stdout, subProcess.stderr,None)
    elif captureSignal:
        return (None,None,_signal)
def cronometrarSubprocess(path:str, cmd:str, realTime:bool = True) -> Tuple[str,float,str]:
    #ok
    command = __makeCommand(path,cmd)
    if realTime:
        realTimeTaken = __realTimer(command)
        return (path,realTimeTaken,"real_time")
    else:
        cpuTimeTaken = __cpuTimer4Linux(command) #depois só deixar disponível a versão do linux de `__cpuTimer4Linux`
        return (path,cpuTimeTaken,"cpu_time")
def obtainSubprocessInfo(execCommand, captureOutput, captureSignal) -> Tuple[Any,Any,Any]:
    #ok
    stdout,stderr,sig = __obtainOutput(execCommand,captureOutput=captureOutput, captureSignal=captureSignal)
    return (stdout,stderr,sig)
    
    """
    if (captureOutput and captureSignal):
        stdout,stderr,sig = __obtainOutput(execCommand,captureOutput=True, captureSignal=True)
        return (stdout,stderr,sig)
    elif (captureOutput):
        stdout,stderr = __obtainOutput(execCommand,captureOutput=True)
        return (stdout,stderr,None)
    elif (captureSignal):
        sig = __obtainOutput(execCommand,captureSignal=True)
        return (None,None,sig)
    """
#FIM: Executor


#INICIO: FAÇADE
def initVariables(concurrent:bool, cpuTime:bool,realTime:bool,captureOutput:bool,captureSignal:bool) -> List[str]:
    execType = "concurrent" if concurrent else "sequential"
    output = "output" if captureOutput else None
    signal = "signal" if captureSignal else None
    metricType = None
    if (cpuTime or realTime):
        metricType = "cpuTime" if cpuTime else "realTime"
    return [execType,metricType,output,signal]
#FIM: FAÇADE


def queue2List(queue:mp.Queue[Any],length) -> List[Any]:
    return [queue.get() for _ in range(length)]