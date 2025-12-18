#import functions.utils.estatisticas as stats
#from classes.runner import Runner
from typing import List, Tuple
import statistics

class Analyser:
    def __init__(self,execTimes=[]):
        self.execTimes:Tuple[str,float] = execTimes
    
    def setExecTimes(self,execTimes):
        self.execTimes = execTimes
    
    def getExecTimes(self):
        return self.execTimes

    def mean(self) -> float:
        return statistics.mean([time[1][1] for time in self.execTimes])

    def stdDevPop(self)->float:
        return statistics.pstdev([time[1][1] for time in self.execTimes])

    def fastest(self) -> Tuple[str,float]:
        return sorted(self.execTimes, key=lambda elem:elem[1][1])[0]

    def slowest(self) -> Tuple[str,float]:
        return sorted(self.execTimes, key=lambda elem:elem[1][1])[-1]