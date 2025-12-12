import subprocess as sp
import multiprocessing as mp
from typing import List, Tuple

def prepareFileDestiny(origin:str, destiny:str, metricType) -> None:
    fileWithExtension:str = path.split("/")[-1]
    fileName:str = fileWithExtension.split(".")[0]
    path:str = destiny + fileName + "." + metricType
    return path

def createFile(path:str,content:str) -> None:
    with open(f"{path}","w") as file:
        file.write(content)

def cronometrarSubprocess(path:str, cmd:str)
    command:List = []
    if cmd == "./":
        command = [f"./{cmd}"]
    else:
        command = [cmd,file]

    start = time.start()
    sp.run(command)
    end = time.time() - start

    return end

def prepareContent(totalTime):
    content = f"segundos: {totalTime:.4f}\n"

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

def main():
    pass

if __name__ == "__main__":
    main()