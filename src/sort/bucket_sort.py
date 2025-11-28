from typing import Callable

def bucket_sort(inner_sort: Callable[[list[float]], list[float]], numbers: list[float], bucket_count: int = 10) -> list[float]:
    """
    Bucket sort для числовых данных (int или float).
    bucket_count должен быть >= 1.
    """
    if bucket_count < 1:
        raise ValueError("bucket_count must be >= 1")

    length = len(numbers)

    if length == 0:
        return []

    if length == 1:
        return numbers.copy()

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return numbers.copy()

    value_range = max_value - min_value

    buckets: list[list[float]] = [[] for _ in range(bucket_count)]

    for value in numbers:
        offset = value - min_value
        relative_position = offset / value_range
        scaled_position = relative_position * bucket_count
        bucket_index = int(scaled_position)

        if bucket_index == bucket_count:
            bucket_index -= 1

        buckets[bucket_index].append(value)

    sorted_buckets = [inner_sort(bucket) for bucket in buckets]

    result = []
    for bucket in sorted_buckets:
        result.extend(bucket)

    return result
