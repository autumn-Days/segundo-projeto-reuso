import utils.estatisticas as stats
from runner.runner import Runner
from typing import List, Tuple

class Analyser:
    def __init__(self, myRunner:"Runner"):
        self.myRunner = myRunner
        self.times:Tuple[str,float] = []

    def mean(self, execTimes:List[float]):
        return stats.mean(execTimes)

    def stdDevPop(self, execTimes:List[float]):
        return stats.stdDevPop(execTimes)
    
    def fastest(self, execTimes:List[float]):
        return stats.fastest(execTimes)
    
    def slowest(self, execTimes:List[float]):
        return stats.slowest(execTimes)