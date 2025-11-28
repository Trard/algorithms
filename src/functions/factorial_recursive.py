from functools import cache

@cache
def factorial_recursive(n: int) -> int:
    """
    Факториал
    """
    if n == 0:
        return 1
    if n == 1:
        return 1

    return factorial_recursive(n-1)*n
