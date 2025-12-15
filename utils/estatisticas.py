import statistics
from typing import List

def mean(execTimes:List[float]):
    return statistics.mean(execTimes)

def stdDevPop(execTimes:List[float]):
    return statistics.pstdev(execTimes)

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

class decorator 


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
