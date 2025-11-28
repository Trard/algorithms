import time
from typing import Callable

def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Измеряет время одного вызова func(*args, **kwargs).
    Возвращает длительность в секундах(float) .
    В случае исключения — исключение пробрасывается наружу.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start
