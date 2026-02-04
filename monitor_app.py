import psutil
import time
import csv
import os
from datetime import datetime
import subprocess

# Start process
start_time = time.time()

# Run workload
process = subprocess.Popen(["python", "app.py"])

ps_proc = psutil.Process(process.pid)

cpu_start = ps_proc.cpu_times()
mem_start = ps_proc.memory_info().rss

# Wait for completion
process.wait()

cpu_end = ps_proc.cpu_times()
mem_end = ps_proc.memory_info().rss
end_time = time.time()

runtime = end_time - start_time
cpu_user = cpu_end.user - cpu_start.user
cpu_system = cpu_end.system - cpu_start.system
memory_used = mem_end - mem_start

timestamp = datetime.utcnow().isoformat()

row = [
    timestamp,
    runtime,
    cpu_user,
    cpu_system,
    memory_used
]

file_exists = os.path.isfile("metrics.csv")

with open("metrics.csv", "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "runtime",
            "cpu_user",
            "cpu_system",
            "memory_used"
        ])

    writer.writerow(row)

print("Metrics recorded:", row)
