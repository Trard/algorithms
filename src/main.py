from src.sort.counting_sort import counting_sort
from src.sort.quick_sort import quick_sort
from src.sort.heap_sort import heap_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.bubble_sort import bubble_sort
from src.sort.radix_sort import radix_sort
from src.benchmark.benchmark import benchmark_sorts
import random
from functools import partial
from sys import setrecursionlimit
from pprint import pprint
from typing import Callable, Any

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    setrecursionlimit(100000)
    bucket_heap_sort = partial(bucket_sort, heap_sort)

    rand_array = []
    balanced_array = []
    low_unique_array = []
    worst_array = []
    best_array = []

    for i in range(10000):
        rand_array.append(random.randint(0, 100000))

    for i in range(10000):
        balanced_array.append(i)

    for i in range(0, 10000):
        low_unique_array.append(random.randint(0, 5))

    for i in range(10000, 0, -1):
        worst_array.append(i)

    for i in range(0, 10000):
        best_array.append(i)


    random.shuffle(balanced_array)

    arrays = {
        "rand": rand_array,
        "balanced": balanced_array,
        "worst": worst_array,
        "best": best_array,
        "low_unique": low_unique_array
    }

    algos: dict[str, Callable[..., Any]] = {
        "bubble": bubble_sort,
        "counting": counting_sort,
        "radix": radix_sort,
        "heap": heap_sort,
        "quick": quick_sort,
        "bucket_heap": bucket_heap_sort
    }

    results = benchmark_sorts(arrays, algos)

    pprint(results)

if __name__ == "__main__":
    main()
