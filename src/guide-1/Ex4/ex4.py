import time

from src.utils import Line, Timer, setup, n
import random


def capicua_recursive(lista: list) -> bool:
    if len(lista) == 0 or len(lista) == 1: return True

    actual = lista[0] == lista[-1]
    if not actual:
        return False

    return capicua_recursive(lista[1:-1])


def capicua_iterative(lista: list) -> bool:
    if len(lista) == 0 or len(lista) == 1: return True

    ptr_left = 0
    ptr_right = len(lista) - 1

    while ptr_left < ptr_right:
        if lista[ptr_left] == lista[ptr_right]:
            ptr_left += 1
            ptr_right -= 1
        else: return False

    return True


Line()
print(capicua_recursive([1, 2]))       # False
print(capicua_recursive([2, 1, 2]))    # True
print(capicua_recursive([1, 2, 2]))    # False
print(capicua_recursive([1, 2, 3]))    # False
Line()


lista = []
setup(10000)
for i in range(n//100):
    lista.append(int(random.random() * 100))
capicua = lista + lista[::-1]


i1 = time.time()
r1 = capicua_recursive(capicua)
e1 = time.time()
print(f"Capicua recursive took {e1-i1:.2f}s - result: {r1}")

lista.clear()
print(f"> n configurado en {10000 * 100 * 10}")
for i in range(n*10):
    lista.append(int(random.random() * 100))
capicua = lista + lista[::-1]

i2 = time.time()
r2 = capicua_iterative(capicua)
e2 = time.time()
print(f"Capicua iterative took {e2-i2:.2f}s - result: {r2}")

Line()

