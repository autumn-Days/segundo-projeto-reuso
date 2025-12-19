import subprocess as sp
from typing import List,Tuple,Any
import signal
from classes.strategy.timerStrategy import timer_selector

#Início: Executor
def _makeCommand(path:str,cmd:str) -> List[str]:
    #ok
    command:List = []
    if cmd == "./":
        command = [f"./{path}"]
    else:
        command = [cmd,path]
    return command

def _obtainOutput(command:List[str],captureOutput=False,captureSignal=False) -> Any : # ((str,str,str),(str,str),str
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

    command = _makeCommand(path,cmd)

    timer, timerType = timer_selector(realTime)

    realTimeTaken = timer.measure(command)
    return (path,realTimeTaken,timerType) #depois só deixar disponível a versão do linux de `__cpuTimer4Linux`
        
def obtainSubprocessInfo(execCommand, captureOutput, captureSignal) -> Tuple[Any,Any,Any]:
    #ok
    stdout,stderr,sig = _obtainOutput(execCommand,captureOutput=captureOutput, captureSignal=captureSignal)
    return (stdout,stderr,sig)
    
    """
    if (captureOutput and captureSignal):
        stdout,stderr,sig = _obtainOutput(execCommand,captureOutput=True, captureSignal=True)
        return (stdout,stderr,sig)
    elif (captureOutput):
        stdout,stderr = _obtainOutput(execCommand,captureOutput=True)
        return (stdout,stderr,None)
    elif (captureSignal):
        sig = _obtainOutput(execCommand,captureSignal=True)
        return (None,None,sig)
    """
#FIM: Executor