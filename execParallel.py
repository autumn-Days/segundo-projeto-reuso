import multiprocessing as mp
from typing import List, Tuple, Callable
#from utils import utils as util
import utils.utils as util
import utils.estatisticas as stats
import time #tirar depois

#por falta de nome melhor
def facadeTime(queue:mp.Queue, origin:str,destiny:str,
    cmd:str,params:List[str],realTime:bool) -> Tuple[str,float]:

    totalTime:float = util.cronometrarSubprocess(origin,cmd,realTime)
    destiny:str = util.createDestinyPath(origin,destiny,params)
    content:str = util.prepareContent(totalTime=totalTime[1])
    util.createFile(destiny,content)
    queue.put((origin,totalTime))


def facadeOutput(queue:mp.Queue, origin:str,destiny:str,
    cmd:str,params:List[str],captureOutput:bool,
    captureSignal:bool) -> Tuple[str,Tuple[str,str,str]]:
    execCommand:str = util.__makeCommand(origin,cmd)
    stdout,stderr,signal = util.obtainSubprocessInfo(execCommand,captureOutput,captureSignal)
    destiny:str = util.createDestinyPath(origin,destiny,params)
    content:str = util.prepareContent(output=(stdout,stderr),signal=signal)
    util.createFile(destiny,content)
    queue.put((origin,(stdout,stderr,signal)))


def execBatch(programs:List[Tuple[str,str,str]],
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

    for origin,destiny,cmd in programs:
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
    return util.queue2List(infos,len(programs))

"""
class Runner:
    def __init__(self, programs:List[Tuple[str,str,str]]) -> None:
        self.programs = programs
    
    def execBatch(self,concurrent:bool=True, cpuTime:bool=False, realTime:bool=False) -> List[Tuple[str,float]]:
        execType, metricType= util.initVariables(concurrent,cpuTime)
        params = [execType,metricType]
        processes = []
        myQueue = mp.Queue() 

        for origin,destiny,cmd in self.programs:
            p = mp.Process(
                target = facade,
                args = (myQueue,origin,destiny,cmd,params,realTime)
            )
            processes.append(p)
            p.start()
            if (not concurrent):
                p.join()
        
        if (concurrent):
            for p in processes:
                p.join()
"""
"""
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


"""
Uma outra funcionalidade legal é implementar os algoritmos no próprio arquivo principal
e depois especificar na biblioteca que se trata de uma leitura "local". Notei que ter
que especificar o path dos arquivos pode ser meio incoviniente para programas pequenos.

Ou também ser possível combinar funções localmente e comparar com os arquivos, mas uma
coisa de cada vez.
"""
"""
programs:List[Tuple[str,str,str]],
concurrent=True,
cpuTime=False,
realTime=False,
captureOutput=False,
captureSignal=False
"""
def main():
    programs = [
        ("codigosTeste/triviais/script1.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script1_defeituoso.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script2.js","codigosTeste/triviais/outputs", "node"),
        ("codigosTeste/triviais/programa1.out","codigosTeste/triviais/outputs","./")
        ]
    
    """
    #Teste da obtenção de outputs
    lista = execBatch(programs,captureOutput=True, captureSignal=True)
    time.sleep(3)
    lista = execBatch(programs,captureOutput=True)
    time.sleep(3)
    lista = execBatch(programs,captureSignal=True)
    time.sleep(3)
    """
    """
    #Teste das estatísticas
    lista = execBatch(programs,concurrent=True, cpuTime=True)
    print(stats.fastest(lista))
    print(stats.slowest(lista))
    print(stats.mean(lista))
    print(stats.stdDevPop(lista))
    """
    
    #Testes dos tipos de execução com tipos de medidas diferentes
    execBatch(programs,concurrent=False, cpuTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=True, realTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=False, realTime=True)
    
if __name__ == "__main__":
    main()