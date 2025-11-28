def counting_sort(list: list[int]) -> list[int]:
    """
    Сортировка целых чисел подсчетом
    """
    if (len(list) == 0):
        return list

    shift = -min(list)

    size = max(list) + 1 + shift
    temp = [0] * size
    result = []

    for el in list:
        index = el + shift

        current_count = temp[index]

        if current_count is None:
            temp[index] = 1
        else:
            temp[index] = current_count + 1

    for index, el in enumerate(temp):
        for i in range(el):
            result.append(index-shift)

    return result
