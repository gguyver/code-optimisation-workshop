import time
from concurrent.futures import ProcessPoolExecutor

def slow_square(x):
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    t1 = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(slow_square, range(5)))
    t2 = time.perf_counter()
    print(f"Parallel execution took {t2 - t1:.4f} seconds")
    print("Results:", results)