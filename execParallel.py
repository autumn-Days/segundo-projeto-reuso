import multiprocessing as mp
from typing import List, Tuple
from utils import utils as util

#por falta de nome melhor
#vai obter o tempo, preparar o path de destino, preparar o conteúdo do arquivo e salvar
def facade(origin:str,destiny:str,cmd:str,params:List[str]) -> None:
    totalTime:float = util.cronometrarSubprocess(origin,cmd)
    destiny:str = util.createDestinyPath(origin,destiny,params)
    content:str = util.prepareContent(totalTime)
    util.createFile(destiny,content)

def execBatch(programs:List[Tuple[str,str,str]], concurrent:bool=True, cpuTime=False, realTime=False) -> None:
    execType = "concurrent" if concurrent else "sequential"
    metricType = "real_time" if realTime else "cpu_time"
    params = [metricType,execType]
    processes = []

    for origin,destiny,cmd in programs:
        p = mp.Process(
            target = facade,
            args = (origin,destiny,cmd,params)
        )
        processes.append(p)
        p.start()
        if (not concurrent):
            p.join()
    
    if (conconrrent):
        for p in processes:
            p.join()

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
    execBatch(programs,concurrent=True, realTime=True)
    execBatch(programs,concurrent=False, realTime=True)

if __name__ == "__main__":
    main()