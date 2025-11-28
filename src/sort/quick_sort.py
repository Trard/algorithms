def quick_sort(list: list[int]) -> list[int]:
    """
    Быстрая сортировка для целых чисел.
    """
    if len(list) <= 1:
        return list

    pivot = list[0]
    less = [x for x in list[1:] if x < pivot]
    more = [x for x in list[1:] if x >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(more)
