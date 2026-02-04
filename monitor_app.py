import psutil
import time
import csv
import os
from datetime import datetime

process = psutil.Process()

# Start measurements
start_time = time.time()
cpu_start = process.cpu_times()
mem_start = process.memory_info().rss

# Simulate monitoring during workload
time.sleep(1)

# End measurements
end_time = time.time()
cpu_end = process.cpu_times()
mem_end = process.memory_info().rss

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
