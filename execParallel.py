import multiprocessing as mp
from typing import List, Tuple
from utils import utils as util
#por falta de nome melhor
#vai obter o tempo, preparar o path de destino, preparar o conteúdo do arquivo e salvar
def facade(origin:str,destiny:str,cmd:str,metricType:str) -> None:
    totalTime:float = util.cronometrarSubprocess(origin,cmd)
    destiny:str = util.prepareFileDestiny(origin,destiny,metricType)
    content:str = util.prepareContent(totalTime)
    util .createFile(destiny,content)

def execBatch(programs:List[Tuple[str,str,str]], cpuTime=False, realTime=False) -> None:
    metricType = "real_time" if realTime else "cpu_time"
    processes = []

    for origin,destiny,cmd in programs:
        p = mp.Process(
            target = facade,
            args = (origin,destiny,cmd,metricType)
        )
        processes.append(p)
        p.start()
    
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
        #("codigosTeste/triviais/script1.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script2.js","codigosTeste/triviais/outputs", "node"),
        ("codigosTeste/triviais/programa1.out","codigosTeste/triviais/outputs","./")
        ]
    execBatch(programs, False, True)

if __name__ == "__main__":
    main()