def bubble_sort(list: list[int]) -> list[int]:
    """
    Сортиовка пузырьком
    """
    cloned_list = list.copy()

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if (cloned_list[j] > cloned_list[j+1]):
                cloned_list[j], cloned_list[j+1] = cloned_list[j+1], cloned_list[j]

    return cloned_list
