def counting_sort_by_digit(numbers: list[int], exponent: int, base: int) -> list[int]:
    """
    Подсортировка по одной цифре.
    """
    length = len(numbers)

    counts = [0] * base
    output = [0] * length

    for number in numbers:
        digit = (number // exponent) % base
        counts[digit] += 1

    for i in range(1, base):
        counts[i] += counts[i - 1]

    for number in reversed(numbers):
        digit = (number // exponent) % base

        counts[digit] -= 1
        position = counts[digit]

        output[position] = number

    return output


def radix_on_nonnegatives(items: list[int], base: int) -> list[int]:
    """
    Radix sort для неотрицательных целых чисел.
    """
    length = len(items)

    if length == 0:
        return []

    max_value = max(items)
    exponent = 1
    result = items.copy()

    while max_value // exponent > 0:
        result = counting_sort_by_digit(result, exponent, base)
        exponent *= base

    return result


def radix_sort(numbers: list[int], base: int = 10) -> list[int]:
    """
    Radix sort для целых чисел.
    Поддерживает отрицательные числа.
    Параметр base должен быть >= 2.
    """
    if base < 2:
        raise ValueError("base must be >= 2")

    if len(numbers) == 0:
        return []

    positives = [n for n in numbers if n >= 0]
    negatives_abs = [-n for n in numbers if n < 0]

    sorted_positives = radix_on_nonnegatives(positives, base)
    sorted_negatives_abs = radix_on_nonnegatives(negatives_abs, base)
    sorted_negatives = [-x for x in reversed(sorted_negatives_abs)]

    return sorted_negatives + sorted_positives
