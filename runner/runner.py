import multiprocessing as mp
from typing import List, Tuple, Any
import utils.utils as util
import reproducer.reproducer as repro
import executor.executor as exec

def facadeTime(queue:mp.Queue, origin:str,destiny:str,
    cmd:str,params:List[str],realTime:bool) -> Tuple[str,float]:
    totalTime:float = exec.cronometrarSubprocess(origin,cmd,realTime)
    destiny:str = repro.createDestinyPath(origin,destiny,params)
    content:str = repro.prepareContent(totalTime=totalTime[1])
    repro.createFile(destiny,content) 
    queue.put((origin,totalTime))


def facadeOutput(queue:mp.Queue, origin:str,destiny:str,
    cmd:str,params:List[str],captureOutput:bool,
    captureSignal:bool) -> Tuple[str,Tuple[str,str,str]]:
    execCommand:str = exec.__makeCommand(origin,cmd)
    stdout,stderr,signal = exec.obtainSubprocessInfo(execCommand,captureOutput,captureSignal)
    destiny:str = repro.createDestinyPath(origin,destiny,params)
    content:str = repro.prepareContent(output=(stdout,stderr),signal=signal)
    repro.createFile(destiny,content)
    queue.put((origin,(stdout,stderr,signal)))


class Runner:
    def __init__(self, programs:List[Tuple[str,str,str]]) -> None:
        self.programs = programs
    
    def execBatch(self,
        concurrent=True,
        cpuTime=False,
        realTime=False,
        captureOutput=False,
        captureSignal=False) -> None:

        #concurrent:bool, cpuTime:bool,realTime:bool,captureOutput:bool,captureSignal:bool
        params = util.initVariables(concurrent,cpuTime,realTime,captureOutput,captureSignal)

        processes = []
        #Essa lista vai guardar todos os dados dos programas
        infos:mp.queue[Any] = mp.Queue()

        for origin,destiny,cmd in self.programs:
            p = None
            if (realTime or cpuTime):
                p = mp.Process(
                    target = facadeTime,
                    args = (infos,origin,destiny,cmd,params,realTime)
                )
            elif (captureOutput or captureSignal):
                p = mp.Process(
                    target = facadeOutput,
                    args = (infos,origin,destiny,cmd,params,captureOutput,captureSignal)
                )
            processes.append(p)
            p.start()
            if (not concurrent):
                p.join()
        
        if (concurrent):
            for p in processes:
                p.join()
        return util.queue2List(infos,len(self.programs))

