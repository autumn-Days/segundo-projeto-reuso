import multiprocessing as mp
from typing import List, Tuple, Any
import functions.utils.utils as util
import functions.reproducer.reproducer as repro
import functions.executor.executor as exec
import functions.utils.estatisticas as stats
import time #tirar depois

from classes.facade.facade import Facade
from classes.runner.runner import Runner
from classes.analyser.analyser import Analyser

#por falta de nome melhor
"""
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
"""

#
"""
def display(content:List[Tuple]):
    typeReproducao = 0 #0 se for de tempo & 1 se for de output
    if type(content[0][1]) == tuple :
        typeReproducao = 1
    if typeReproducao:
        for con in content:
"""            

"""
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
    
    
    #TESTE COM CLASSES INDIVIDUAIS
    """ 
    runner = Runner(programs)
    lista = runner.execBatch(concurrent=True, cpuTime=True)

    analyser = Analyser(runner)
    print(analyser.mean(lista))
    """
    

    #Teste das estatísticas
    #está pegando
    """
    lista = execBatch(programs, concurrent=True, cpuTime=True)
    print(stats.fastest(lista))
    print(stats.slowest(lista))
    print(stats.mean(lista))
    print(stats.stdDevPop(lista))
    """

    interface = Facade()

    interface.setPrograms(programs)
    lista = interface.runBatch(captureOutput=True, captureSignal=True)
    print(lista)

    interface.print_stats(mean=True,stdDevPop=True,slowest=True,fastest=True)
    
    
    #Testes dos tipos de execução com tipos de medidas diferentes
    #Está pegando
    """
    execBatch(programs,concurrent=False, cpuTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=True, realTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=False, realTime=True)
    """
    
if __name__ == "__main__":
    main()