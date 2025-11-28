from functools import cache

@cache
def fibo_recursive(n: int) -> int:
    if (n <= 1):
        return 0
    if n == 2:
        return 1

    return fibo_recursive(n-1) + fibo_recursive(n-2)
