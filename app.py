import time
import math

def workload():
    total = 0
    for i in range(1_000_000):
        total += math.sqrt(i)
    time.sleep(2)
    return total

if __name__ == "__main__":
    result = workload()
    print("Workload result:", result)
