import statistics
from typing import List

def mean(execTimes:[List[Tuple,str]]) -> float:
    return statistics.mean([time[1][1] for time in execTimes])

def stdDevPop(execTimes:[List[Tuple,str]])->float:
    return statistics.pstdev([time[1][1] for time in execTimes])

def fastest(execTimes:[List[Tuple,str]]) -> Tuple[str,float]:
    return sorted(execTimes, key=lambda elem:elem[1][1])[0]

def slowest(execTimes:List[Tuple[str,float]]) -> Tuple[str,float]:
    return sorted(execTimes, key=lambda elem:elem[1][1])[-1]

#por falta de nome melhor
"""
É importante . Para incluir essa funcionalidade, eu vou ter que por ainda mais parâmetros]
na entrada do façade. Talvez seja até bom usar um decorator tipo

myStatistics = Estatisticas(ExecutorParalelo)

Internamente, ele salvaria todos os outputs de tempo como uma lista de tuplas

[(programa1,tempo1),(programa2,tempo2),(programa3,tempo3)]

e depois pode dar para usar algo do tipo

myStatics.mean()
myStatics.stdDevPop()
myStatics.min()
myStatics.max()

E a classe façade pode implementar um método que vai transformar isso tudo em uma string
e imprimir
"""

#class decoratorStat:
#    def __init__(self,)

"""
Essa daqui eu deixo para você implementar, Marcelo
É só questão de salvar esse conteúdo em um arquivo/imprimir no terminal
def statisticsFacade(execTimes:List[float],mean_=False, stdDevPop_=False, min_=False, max_=False):
    content = ""
    if mean_ :
        content += f"Mean: {mean(execTimes)}\n"
    if stdDevPop_:
        content += f"Population Standard Deviation: {stdDevPop(execTimes)}\n"
    if min_:
        content += f"Min: {min(execTimes)}\n"
    if max_:
        content += f"Max: {max(execTimes)}\n"
    return content
"""