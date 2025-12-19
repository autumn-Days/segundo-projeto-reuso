from classes.runner import Runner
from classes.analyser import Analyser

class Facade:
    def __init__(self, programs=None):
        self.runner = Runner(programs)
        self.analyser = Analyser()
        self.results = None
        self.concurrent = True
        self.dataType = None #"Time" se o tempo for obtido, "Output" se a saída for obtida

    def setPrograms(self, programs):
        self.runner.programs = programs

    def runBatch(self,
            cpuTime=False,
            realTime=False,
            captureOutput=False,
            captureSignal=False) -> None:

        if (realTime and cpuTime):
            raise ValueError("Combinação inválida de parâmetros: só é possível escolher uma métrica de tempo.")
        if (realTime or cpuTime):
            self.dataType = "TIME"
        elif (captureOutput or captureSignal):
            self.dataType = "OUTPUT"

        self.results = self.runner.execBatch(self.concurrent,cpuTime,realTime,captureOutput,captureSignal)

    def setSequentialBatch(self):
        self.concurrent = False

    def setConcurrentBatch(self):
        self.concurrent = True
    
    def getResults(self):
        return self.results

    def calcStats(self, mean=False, stdDevPop=False, slowest=False, fastest=False):
        if self.results is None:
            raise TypeError("Nenhum dado obtido. Você rodou o 'runBatch'?")
        if self.dataType != "TIME":
            raise TypeError("Operação inválida. Não é possível obter estatíticas numéricas com outputs.")
        
        stats = []
        self.analyser.setExecTimes(self.results)
        if mean :
            mean_ = self.analyser.mean() 
            stats.append(mean_)
        if stdDevPop :
            stdDevPop_ = self.analyser.stdDevPop() 
            stats.append(stdDevPop_)
        if slowest :
            slowest_ = self.analyser.slowest() 
            stats.append(slowest_)
        if fastest :
            fastest_ = self.analyser.fastest()
            stats.append(fastest_)
        return tuple(stats)

