from src.utils import Line, Timer, setup, n

setup(1000000)


def ex_A_recursive(n):
    if n == 1: return 1
    return ex_A_recursive(n - 1) + n


def ex_A_iter(n):
    count = 0
    for i in range(n + 1):
        count += i
    return count


def ex_B_recursive(n):
    if n == 1: return 1
    return ex_B_recursive(n - 1) + n ** 2


def ex_B_iter(n):
    count = 0
    for i in range(n + 1):
        count += i ** 2
    return count


def ex_C_recursive(n, p):
    if n == 0: return 1

    return ex_C_recursive(n - 1, p) + p**n


def ex_C_iter(n, p):
    count = 0
    for i in range(n + 1):
        count += p ** i
    return count


Line()

# * Ej. A
Timer("a", ex_A_recursive, True)
Timer("a", ex_A_iter, False)
Line()

# * Ej. B
Timer("b",  ex_B_recursive, True)
Timer("b", ex_B_iter, False)
Line()

setup(50000)

# * Ej. C
Timer("c", ex_C_recursive, True, 2)
Timer("c", ex_C_iter, False, 2)
Line()
