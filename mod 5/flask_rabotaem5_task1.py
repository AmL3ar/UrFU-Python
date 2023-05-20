#task 1

import subprocess
import os


def start_server(port):
    port_used = check_port_used(port)
    
    if port_used:
        process_id = port_used[1]
        kill_process(process_id)

    start_server_command = f"python flask_rabotaem5.py --port {port}"
    subprocess.call(start_server_command, shell=True)


def check_port_used(port):
    command = f"lsof -i :{port}"
    res = subprocess.run(command, shell=True, capture_output=True, text=True)

    if res.returncode == 0 and res.stdout:
        process_info = res.stdout.strip().split("\n")[1]
        process_id = int(process_info.split()[1])
        return True, process_id

    return False


def kill_process(process_id):
    os.kill(process_id, 9)
