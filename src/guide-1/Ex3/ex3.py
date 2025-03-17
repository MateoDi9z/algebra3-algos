import time

from src.utils import Line, Timer, setup, n


def cero_counter_recursive(num: int):
    if num < 10: return 1 if num == 0 else 0
    return cero_counter_recursive(num // 10) + (1 if num % 10 == 0 else 0)


def cero_counter_iterative(num: int):
    counter = 0
    i = num
    while i > 10:
        if i % 10 == 0:
            counter += 1
        i = i // 10
    return counter


Line()
print(f"recursive - num={2302} -> {cero_counter_recursive(2302)}")         # 1
print(f"recursive - num={2302} -> {cero_counter_recursive(2006302)}")      # 3
print(f"recursive - num={2302} -> {cero_counter_recursive(230020)}")       # 3
print(f"recursive - num={2302} -> {cero_counter_recursive(23032102)}")     # 2
Line()
print(f"iterative - num={2302} -> {cero_counter_iterative(2302)}")         # 1
print(f"iterative - num={2302} -> {cero_counter_iterative(2006302)}")      # 3
print(f"iterative - num={2302} -> {cero_counter_iterative(230020)}")       # 3
print(f"iterative - num={2302} -> {cero_counter_iterative(23032102)}")     # 2
Line()

setup(10000)

numero = 938218903801293890128903890128903890129803891209382189038012938901289038901289038901298038912093821890380129389012890389012890389012980389120938218903801293890128903890128903890129803891209382189038012938901289038901289038901298038912093821890380129389012890389012890389012980389120
numero = numero**150

i1 = time.time()
r1 = cero_counter_recursive(numero)
e1 = time.time()

i2 = time.time()
r2 = cero_counter_iterative(numero)
e2 = time.time()

print(f"Time recursive: {round(e1-i1, 3)}s")
print("resultado:", r1)
print(f"Time iterative: {round(e2-i2, 3)}s")
print("resultado:", r2)
