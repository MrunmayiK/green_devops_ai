import psutil
import time
import csv
import os
import subprocess
from datetime import datetime

# Start workload
start_time = time.time()
process = subprocess.Popen(["python", "app.py"])

ps_proc = psutil.Process(process.pid)

cpu_user = 0.0
cpu_system = 0.0
peak_memory = 0

# Monitor while running
while process.poll() is None:
    try:
        cpu = ps_proc.cpu_times()
        mem = ps_proc.memory_info().rss

        cpu_user = cpu.user
        cpu_system = cpu.system
        peak_memory = max(peak_memory, mem)

    except psutil.NoSuchProcess:
        break

    time.sleep(0.1)

end_time = time.time()
runtime = end_time - start_time

timestamp = datetime.utcnow().isoformat()
mode = os.getenv("WORKLOAD_MODE", "normal")
row = [
    timestamp,
    mode,
    runtime,
    cpu_user,
    cpu_system,
    peak_memory
]

file_exists = os.path.isfile("metrics.csv")

with open("metrics.csv", "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "mode",
            "runtime",
            "cpu_user",
            "cpu_system",
            "peak_memory"
        ])

    writer.writerow(row)

print("Metrics recorded:", row)
