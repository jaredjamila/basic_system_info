#!/usr/bin/env python3
# system_info.py
# A simple script to display basic system information

import platform
import psutil
import socket

def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname())
    }
    return info

def print_system_info():
    info = get_system_info()
    print("=== System Information ===")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print_system_info()
