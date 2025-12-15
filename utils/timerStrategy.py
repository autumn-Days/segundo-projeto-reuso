from abc import ABC, abstractmethod
from typing import List
import subprocess as sp
import os
import time
import psutil
from typing import List

class TimerStrategy(ABC):
    @abstractmethod
    def measure(self, command: List[str]) -> float:
        pass

class RealTimeStrategy(TimerStrategy):
    def measure(self, command: List[str]) -> float:
        start = time.time()
        sp.run(command)
        return time.time() - start


class CpuTimeLinuxStrategy(TimerStrategy):
    def measure(self, command: List[str]) -> float:
        sub_process = sp.Popen(command)
        _, _, rusage = os.wait4(sub_process.pid, 0)
        return rusage.ru_utime + rusage.ru_stime


class CpuTimeWindowsStrategy(TimerStrategy):
    def measure(self, command: List[str]) -> float:
        sub_process = psutil.Popen(command)
        sub_process.wait()
        cpu_time = sub_process.cpu_times()
        return cpu_time.user + cpu_time.system
