from typing import List,Any
import multiprocessing as mp

#INICIO: FAÇADE
def initVariables(concurrent:bool, cpuTime:bool,realTime:bool,captureOutput:bool,captureSignal:bool) -> List[str]:
    execType = "concurrent" if concurrent else "sequential"
    output = "output" if captureOutput else None
    signal = "signal" if captureSignal else None
    metricType = None
    if (cpuTime or realTime):
        metricType = "cpuTime" if cpuTime else "realTime"
    return [execType,metricType,output,signal]
#FIM: FAÇADE


def queue2List(queue:mp.Queue[Any],length) -> List[Any]:
    return [queue.get() for _ in range(length)]