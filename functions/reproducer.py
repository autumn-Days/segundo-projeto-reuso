import subprocess as sp
from typing import List,Tuple

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
    return f"{suffix}.txt"
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
    if (output != (None,None) and (totalTime == None)):
        stdout = output[0]
        stderr = output[1]
        content += f"stdout:\n\n{stdout}\n\n"
        content += f"stderr:\n\n{stderr}\n\n"
    if signal:
        content += f"signal:\n\t{signal}\n"
    return content

#def display(origin)
#FIM: funções de Reprodutor