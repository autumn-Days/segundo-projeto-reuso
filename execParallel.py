import multiprocessing as mp
from typing import List, Tuple, Callable
from utils import utils as util
import time #tirar depois

#por falta de nome melhor
def facade(conn:mp.Queue, origin:str,destiny:str,cmd:str,params:List[str],realTime=False) -> Tuple[str,float]:
    totalTime:float = util.cronometrarSubprocess(origin,cmd,realTime)
    destiny:str = util.createDestinyPath(origin,destiny,params)
    content:str = util.prepareContent(totalTime)
    util.createFile(destiny,content)
    queue.put((destiny,totalTime))

def execBatch(programs:List[Tuple[str,str,str]], concurrent:bool=True, cpuTime:bool=False, realTime:bool=False) -> None:
    execType, metricType= util.initVariables(concurrent,cpuTime)
    params = [execType,metricType]
    processes = []
    times:mp.queue[Tuple[str,float]] = mp.Queue()

    for origin,destiny,cmd in programs:
        p = mp.Process(
            target = facade,
            args = (times,origin,destiny,cmd,params,realTime)
        )
        processes.append(p)
        p.start()
        if (not concurrent):
            p.join()
    
    if (concurrent):
        for p in processes:
            p.join()
    return util.queue2List(times)


class Runner:
    def __init__(self, programs:List[Tuple[str,str,str]]) -> None:
        self.programs = programs
    
    def execBatch(self,concurrent:bool=True, cpuTime:bool=False, realTime:bool=False) -> List[Tuple[str,float]]:
        execType, metricType= util.initVariables(concurrent,cpuTime)
        params = [execType,metricType]
        processes = []

        for origin,destiny,cmd in self.programs:
            p = mp.Process(
                target = facade,
                args = (origin,destiny,cmd,params,realTime)
            )
            processes.append(p)
            p.start()
            if (not concurrent):
                p.join()
        
        if (concurrent):
            for p in processes:
                p.join()

#serve como decorator
class Analyser:
    def __init__(self, myRuner:"Runner"):
        self.myRunner = myRunner
        self.times:Tuple[str,float] = []


    def mean(execTimes:List[float]):
        return statistics.mean(execTimes)

    def stdDevPop(execTimes:List[float]):
        return statistics.pstdev(execTimes)



"""
Uma outra funcionalidade legal é implementar os algoritmos no próprio arquivo principal
e depois especificar na biblioteca que se trata de uma leitura "local". Notei que ter
que especificar o path dos arquivos pode ser meio incoviniente para programas pequenos.

Ou também ser possível combinar funções localmente e comparar com os arquivos, mas uma
coisa de cada vez.
"""
def main():
    programs = [
        ("codigosTeste/triviais/script1.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script2.js","codigosTeste/triviais/outputs", "node"),
        ("codigosTeste/triviais/programa1.out","codigosTeste/triviais/outputs","./")
        ]
    print(execBatch(programs,concurrent=True, cpuTime=True))
    time.sleep(3)
    execBatch(programs,concurrent=False, cpuTime=True)
    time.sleep(1)
    execBatch(programs,concurrent=True, realTime=True)
    time.sleep(1)
    execBatch(programs,concurrent=False, realTime=True)

if __name__ == "__main__":
    main()