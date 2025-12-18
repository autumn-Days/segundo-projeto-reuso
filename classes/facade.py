from classes.runner import Runner
from classes.analyser import Analyser

class Facade:
    def __init__(self, programs=None):
        self.runner = Runner(programs)
        self.analyser = Analyser()
        self.results = None
        self.concurrent = True

    def setPrograms(self, programs):
        self.runner.programs = programs

    def runBatch(self,
            cpuTime=False,
            realTime=False,
            captureOutput=False,
            captureSignal=False) -> None:
        if realTime == cpuTime :
            realTime, cpuTime = True, False

        self.results = self.runner.execBatch(self.concurrent,cpuTime,realTime,captureOutput,captureSignal)

    def setSequentialBatch(self):
        self.concurrent = False

    def setConcurrentBatch(self):
        self.concurrent = True
    
    def getResults(self):
        return self.results

    def calcStats(self, mean=False, stdDevPop=False, slowest=False, fastest=False):
        if self.results is None:
            raise TypeError("results has None type. Have you runned batch?")

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

