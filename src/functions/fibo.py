import math

def fibo(n: int) -> int:
    """
    Функция фибоначчи, которая использует характеристическое уравнение.
    Есть ограничение по точности
    """
    n = n - 1

    num = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)

    return round(num)
