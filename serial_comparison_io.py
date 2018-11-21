import time
from concurrent.futures import ThreadPoolExecutor


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def simulate_io(x):
    print('I am', x)
    time.sleep(3)


n_jobs = 4

marker = time.time()
for i in range(n_jobs): simulate_io(i)
print("Serial spent", time.time() - marker)
marker = time.time()
multithreading(simulate_io, range(n_jobs), 4)
print("Multithreading spent", time.time() - marker)
