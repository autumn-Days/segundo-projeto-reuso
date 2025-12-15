import platform
from utils.timerStrategy import RealTimeStrategy, CpuTimeLinuxStrategy, CpuTimeWindowsStrategy


def create_timer(cpu_time: bool):
    if not cpu_time:
        return RealTimeStrategy()

    if platform.system() == "Windows":
        return CpuTimeWindowsStrategy()
    else:
        return CpuTimeLinuxStrategy()
