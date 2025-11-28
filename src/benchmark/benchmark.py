from typing import Callable
from src.benchmark.timeit_once import timeit_once

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    """
    Бенчмарк сортировок.

    Возвращает: {algo_name: {array_name: avg_seconds}}
    avg_seconds - среднее время
    """
    results: dict[str, dict[str, float]] = {a_name: {} for a_name in algos.keys()}

    for arr_name, arr in arrays.items():
        for algo_name, algo in algos.items():
            arr_copy = list(arr)

            time = timeit_once(algo, arr_copy)

            results[algo_name][arr_name] = time

    return results
