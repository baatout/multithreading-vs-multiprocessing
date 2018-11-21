import time
from concurrent.futures import ThreadPoolExecutor


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def cpu_heavy(x):
    print('I am', x)
    count = 0
    for i in range(10**10):
        count += i


n_jobs = 4

marker = time.time()
for i in range(n_jobs): cpu_heavy(i)
print("Serial spent", time.time() - marker)
marker = time.time()
multithreading(cpu_heavy, range(n_jobs), 4)
print("Multithreading spent", time.time() - marker)
