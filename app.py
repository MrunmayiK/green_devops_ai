import time
import math
import os


MODE = os.getenv("WORKLOAD_MODE", "normal")


def workload():
    total = 0

    if MODE == "light":
        n = 200_000
        sleep = 0.5

    elif MODE == "heavy":
        n = 5_000_000
        sleep = 3

    elif MODE == "memory":
        data = [i for i in range(2_000_000)]
        time.sleep(1)
        return sum(data)

    else:  # normal
        n = 1_000_000
        sleep = 2

    for i in range(n):
        total += math.sqrt(i)

    time.sleep(sleep)

    return total


if __name__ == "__main__":
    result = workload()
    print("Mode:", MODE)
    print("Workload result:", result)
