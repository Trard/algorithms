def heapify(A, heap_size, i):
    """
    Сортирует часть дерева
    """
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, heap_size, largest)


def build_max_heap(A):
    """
    Подготавливает кучу перед сортировкой
    """
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    """
    Сортировка кучей
    """
    n = len(A)
    build_max_heap(A)
    for end in range(n - 1, 0, -1):
        A[0], A[end] = A[end], A[0]
        heapify(A, end, 0)

    return A
