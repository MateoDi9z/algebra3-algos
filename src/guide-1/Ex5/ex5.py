import random
import time

from src.utils import Line, Timer, setup, n
large = 20000
lista = []
setup(large)
for i in range(large):
    lista.append(int(random.random() * 100))


def busquedad_recursiva(lista, num):
    if lista[0] == num:
        return True
    if lista[-1] == num:
        return True

    if 0 < len(lista) <= 2:
        return False

    return busquedad_recursiva(lista[1:-1], num)


def busquedad_iterativa(lista, num):
    for i in lista:
        if i == num:
            return True
    return False


i1 = time.time()
r1 = busquedad_recursiva(lista, 100)
e1 = time.time()
print(f"Busquedada recursiva: {r1} - {e1-i1}s")

i2 = time.time()
r2 = busquedad_iterativa(lista, 100)
e2 = time.time()
print(f"Iterativa: {r2} - {e2-i2}s")