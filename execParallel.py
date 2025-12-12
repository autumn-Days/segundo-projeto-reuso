import subprocess as sp
import multiprocessing as mp
import time
from typing import List, Tuple

def prepareFileDestiny(origin:str, destiny:str, metricType) -> None:
    fileWithExtension:str = origin.split("/")[-1]
    fileName:str = fileWithExtension.split(".")[0]
    path:str = destiny + fileName + "." + metricType
    return path

def createFile(path:str,content:str) -> None:
    with open(f"{path}","w") as file:
        file.write(content)

def cronometrarSubprocess(path:str, cmd:str) -> float:
    command:List = []
    if cmd == "./":
        command = [f"./{cmd}"]
    else:
        command = [cmd,path]

    start = time.time()
    sp.run(command)
    end = time.time() - start

    return end

def prepareContent(totalTime):
    return f"segundos: {totalTime:.4f}\n"

#por falta de nome melhor
#vai obter o tempo, preparar o path de destino, preparar o conteúdo do arquivo e salvar
def facade(origin:str,destiny:str,cmd:str,metricType:str) -> None:
    totalTime:float = cronometrarSubprocess(origin,cmd)
    destiny:str = prepareFileDestiny(origin,destiny,metricType)
    content:str = prepareContent(totalTime)
    createFile(destiny,content)

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
    
    for p in process:
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
    execBatch(programs)

if __name__ == "__main__":
    main()