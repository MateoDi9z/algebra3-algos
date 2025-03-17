from src.utils import Line, Timer, setup


def ex_A_recursive(n):  # n factorial
    if n == 0: return 1
    if n == 1: return 1
    return n * ex_A_recursive(n - 1)


def ex_A_iter(n):
    count = 1
    i = n

    while i > 1:
        count *= i
        i -= 1

    return count


def ex_B_recursive(n):  # 2^n
    if n == 0: return 1
    return ex_B_recursive(n - 1) * 2


def ex_B_iter(n):
    count = 1
    for i in range(n):
        count *= 2
    return count


def fibonacci(n):
    if n == 0 or n == 1: return n
    return fibonacci(n-1) + fibonacci(n-2)


def ex_C_recursive(n):  # Fibonacci
    if n == 1 or n == 0: return n
    return fibonacci(n) + ex_C_recursive(n-1)


def ex_C_iter(n):
    if n == 0: return 0
    if n == 1: return 1

    count = 0
    prev1 = 0
    prev2 = 1
    i = 0

    while i <= n-1:
        point = prev1 + prev2
        count += point
        prev2 = prev1
        prev1 = point
        i += 1

    return count

Line()

# * Ej. A
setup(100000)
Timer("a", ex_A_recursive, True)
Timer("a", ex_A_iter, False)
Line()

# * Ej. B
setup(100000)
Timer("b", ex_B_recursive, True)
Timer("b", ex_B_iter, False)
Line()

# * Ej. C
setup(30)
Timer("c", ex_C_recursive, True)
setup(200000)
Timer("c", ex_C_iter, False)
Line()

