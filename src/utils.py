import time
import sys


n = 1000000


def setup(t=n):
    global n
    n = t
    print(f"> n configurado en {n}")
    sys.setrecursionlimit(t + 10)


def Line(): print("================================")


def Timer(ex: str, f, recursive: bool, param=False):
    ini = time.time()

    if param:
        result = f(n, param)
    else:
        result = f(n)

    end = time.time()

    if recursive:
        print(f"{ex}) recurs. time: \t{round(end - ini, 4)}s")
    else:
        print(f"{ex}) iter. time: \t\t{round(end - ini, 4)}s")
