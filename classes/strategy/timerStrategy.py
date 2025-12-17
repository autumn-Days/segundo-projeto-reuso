from abc import ABC, abstractmethod
from typing import List
import subprocess as sp
import os
import time
from typing import List, Tuple

class TimerStrategy(ABC):
    @abstractmethod
    def measure(self, command: List[str]) -> float:
        pass

class RealTimeStrategy(TimerStrategy):
    def measure(self, command: List[str]) -> float:
        start = time.time()
        sp.run(
            command,
            stdout=sp.PIPE,
            stderr=sp.PIPE)
        end = time.time() - start
        return end

class CpuTimeLinuxStrategy(TimerStrategy):
    def measure(self, command: List[str]) -> float:
        subProcess = sp.Popen(
            command,
            stdout=sp.PIPE,
            stderr=sp.PIPE)
        _, _, rusage = os.wait4(subProcess.pid, 0)
        cpuTime = rusage.ru_utime + rusage.ru_stime
        return cpuTime
    
def timer_selector(realTime: bool) -> Tuple[TimerStrategy, str]:
    if realTime :
        return RealTimeStrategy(), "real_time"
    else :
        return CpuTimeLinuxStrategy(), "cpu_time"