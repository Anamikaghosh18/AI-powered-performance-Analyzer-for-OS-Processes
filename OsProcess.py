import time
from logging import currentframe

import psutil


# This function will show the usage of the cpu
def cpu(cpu_usage, bars = 50):
    # For calculation of cpu percent
    cpu_percent = (cpu_usage / 100.0)
    # For showing the bars of the Cpu usage
    cpu_bar = '|' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    print(f"CPU USAGE: |{cpu_bar}| {cpu_usage:.2f}% ")


# This function will show the usage of the memory
def memory(memory_usage, bars = 50):
    # For calculation of memory percent
    memory_percent = (memory_usage / 100.0)
    # For showing the bars of the memory usage
    memory_bar = '|' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))

    print(f"MEMORY USAGE: |{memory_bar}| {memory_usage: .2f}% ")


# This function will show the usage of the disk
def disk(disk_usage ,bars = 50):
    # For calculation of cpu percent
    disk_percent = (disk_usage / 100.0)
    # For showing the bars of the Cpu usage
    disk_bar = '|' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))

    print(f"DISK USAGE: |{disk_bar}| {disk_usage: .2f}% ")


# This function will show the usage of the cpu
def network(network_usage, bars = 50):
    # For calculation of cpu percent
    network_kbps = (network_usage / 1024)
    max = 1000
    network_percent =  min(network_kbps / max , 1)
    # For showing the bars of the Cpu usage
    network_bar = '|' * int(network_kbps * bars) + '-' * (bars - int(network_percent * bars))
    print(f"NETWORK USAGE: {network_bar} | {network_usage/1024:.2f} KB/s", end="\r")

previous_net = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent


def all_processes(all_processes_usage):
    # This function will show all the processes running in the system
    for process in psutil.process_iter():
        try:
            process_name = process.name()
            process_id = process.pid
            process_status = process.status()
            process_username = process.username()
            process_memory = process.memory_info().rss
            process_cpu = process.cpu_percent()
            print(f"Process Name: {process_name} | Process ID: {process_id} | Process Status: {process_status} | Process Username: {process_username} | Process Memory: {process_memory} | Process CPU: {process_cpu}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


# calculate the usage in every 1 sec
while True:
        cpu(psutil.cpu_percent())
        time.sleep(1)

        memory(psutil.virtual_memory().percent)
        time.sleep(1)

        disk(psutil.disk_usage('/').percent)
        time.sleep(1)

        # to calculate each network use
        current_net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        usage_net = current_net - previous_net
        previous_net = current_net
        network(usage_net, 50)
        # to show all processes running in the system
        all_processes(psutil.process_iter())
        print("\n" + "-" * 50)
        time.sleep(1)
