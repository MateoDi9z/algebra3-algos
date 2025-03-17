from src.utils import Line, Timer, setup


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

    return ex_C_recursive(n - 1, p) + p ** n


def ex_C_iter(n, p):
    count = 0
    for i in range(n + 1):
        count += p ** i
    return count


def ex_D_recursive(n):
    if n == 1: return 1
    return ex_D_recursive(n - 1) + (2 * n - 1)


def ex_D_iter(n):
    count = 0
    i = n
    while i >= 1:
        count += (2 * i) - 1
        i -= 1
    return count


def ex_E_recursive(n):
    if n == 1: return 2
    return ex_E_recursive(n - 1) + n * (n + 1)


def ex_E_iter(n):
    count = 0
    i = n
    while i >= 1:
        count += i + (i + 1)
        i -= 1
    return count


def ex_F_recursive(n):
    if n == 1: return 1
    return ex_F_recursive(n - 1) + n**3


def ex_F_iter(n):
    count = 0
    for i in range(n + 1):
        count += i**3
    return count


Line()

# * Ej. A
setup(10000000)
Timer("a", ex_A_recursive, True)
Timer("a", ex_A_iter, False)
Line()

# * Ej. B
setup(10000000)
Timer("b", ex_B_recursive, True)
Timer("b", ex_B_iter, False)
Line()

# * Ej. C
setup(50000)
Timer("c", ex_C_recursive, True, 2)
Timer("c", ex_C_iter, False, 2)
Line()

# * Ej. D
setup(10000000)
Timer("d", ex_D_recursive, True)
Timer("d", ex_D_iter, False)
Line()

# * Ej. E
setup(10000000)
Timer("e", ex_E_recursive, True)
Timer("e", ex_E_iter, False)
Line()

# * Ej. F
setup(10000000)
Timer("f", ex_F_recursive, True)
Timer("f", ex_F_iter, False)
Line()