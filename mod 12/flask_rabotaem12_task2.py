import multiprocessing
from multiprocessing.pool import ThreadPool, Pool
import subprocess
import os

# memory_usage = 0

def process_count(username: str) -> int:
    output = subprocess.check_output(["ps", "-u", username, "-o", "pid="])
    return len(output.splitlines())


def total_memory_usage(root_pid: int) -> float:
    # global memory_usage
    memory_usage = 0
    pids_command = f"pgrep -P {root_pid}"
    pids_output = os.popen(pids_command).read()
    pids = pids_output.strip().split('\n')
    if pids == ['']:
        pids = []
    pids.append(str(root_pid))
    # with Pool(processes=multiprocessing.cpu_count()) as pool:
    #     pool.map(get_memory_usage_by_pid, pids)
    for pid in pids:
        ps_command = f"ps -p {pid} -o rss="
        ps_output = os.popen(ps_command).read()
        if ps_output != '':
            memory_usage += int(ps_output)
    output = os.popen("free -k").readlines()
    total_memory = output[1]
    total_memory = total_memory.split()[2]
    total_memory = int(total_memory)
    return round(memory_usage/total_memory, 2) * 100


# def get_memory_usage_by_pid(pid):
#     global memory_usage
#     ps_command = f"ps -p {pid} -o rss="
#     ps_output = os.popen(ps_command).read()
#     memory_usage += int(ps_output)


print(total_memory_usage(3227))