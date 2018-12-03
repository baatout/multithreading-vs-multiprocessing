import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

urls = ['http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal',
        'http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal'
        ]


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def load_url(x):
    # print('I am', x)
    with urllib.request.urlopen(urls[x], timeout=20) as conn:
        return conn.read()


n_jobs = len(urls)

marker = time.time()
for i in range(n_jobs): load_url(i)
print("Serial spent", time.time() - marker)
for n_threads in [4, 8, 16]:
    marker = time.time()
    multithreading(load_url, range(n_jobs), n_threads)
    print("Multithreading {} spent".format(n_threads), time.time() - marker)
