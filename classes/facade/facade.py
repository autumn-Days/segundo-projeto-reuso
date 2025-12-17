from classes.runner.runner import Runner
from classes.analyser.analyser import Analyser

class Facade:
    def __init__(self, programs=None):
        self.runner = Runner(programs)
        self.analyser = Analyser(self.runner)
        self.results = None
        self.concurrent = True

    def setPrograms(self, programs):
        self.runner.programs = programs
    
    def runBatch(self,
            concurrent=True,
            cpuTime=False,
            realTime=False,
            captureOutput=False,
            captureSignal=False) -> None:
        if realTime == cpuTime :
            realTime, cpuTime = True, False

        self.concurrent = concurrent

        self.results = self.runner.execBatch(self.concurrent,cpuTime,realTime,captureOutput,captureSignal)
        return self.results

    def setConcurrentBatch(self):
        self.concurrent = True
    
    def setSequentialBatch(self):
        self.concurrent = False

    def print_stats(self, mean=False, stdDevPop=False, slowest=False, fastest=False):
        """     Aqui está comentado apenas para preservar o código puro, sem o print
        if mean :
            self.analyser.mean(self.results)
        if stdDevPop :
            self.analyser.stdDevPop(self.results)
        if fastest :
            self.analyser.fastest(self.results)
        if slowest :
            self.analyser.slowest(self.results)
        """
        if mean :
            print(self.analyser.mean(self.results))
        if stdDevPop :
            print(self.analyser.stdDevPop(self.results))
        if fastest :
            print(self.analyser.fastest(self.results))
        if slowest :
            print(self.analyser.slowest(self.results))
