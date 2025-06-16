import time

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

def verify_fib():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(10) == 55

print(verify_fib())
# using time.perf_counter() and time.process_time()

t1 = time.perf_counter(), time.process_time()
fibonacci(35)
t2 = time.perf_counter(), time.process_time()
print(f"Wall clock time: {t2[0] - t1[0]:.4f} seconds")
print(f"CPU time: {t2[1] - t1[1]:.4f} seconds")

from timeit import timeit
total_time = timeit("fibonacci(30)", number=100, globals=globals())
print(f"Total time for 100 runs: {total_time:.4f} seconds, average time {total_time / 100:.4f} seconds")

# Using cProfile
import cProfile
cProfile.run("fibonacci(35)")

# if you provide a filename to the run() method, it will save the profiling results to a file
cProfile.run("fibonacci(35)", "fibonacci_profile.prof")
# You can then use the pstats module to read and analyze the profiling results
import pstats
p = pstats.Stats("fibonacci_profile.prof")
p.strip_dirs().sort_stats("cumulative").print_stats(10)
# You can also use the pstats module to filter the results by a specific function
p.sort_stats("cumulative").print_stats("fibonacci")