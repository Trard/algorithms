from src.constants import LOAD_FACTOR
from src.constants import MIN_LOAD

"""
Очередь на списке
"""
class ListQueue:
    def __init__(self):
        self._data = []
        self._head: int = 0

    def enqueue(self, x: int):
        """Добавить элемент в конец очереди."""
        self._data.append(x)

    def dequeue(self) -> int:
        """Удалить и вернуть элемент из начала очереди.
        Бросает IndexError, если очередь пустая."""
        if self.is_empty():
            raise IndexError()

        val = self._data[self._head]
        self._head += 1

        if self._head > MIN_LOAD and self._head > len(self._data) * LOAD_FACTOR:
            self._data = self._data[self._head:]
            self._head = 0

        return val

    def front(self) -> int:
        """Вернуть элемент из начала очереди без удаления.
        Бросает IndexError, если очередь пустая."""
        if self.is_empty():
            raise IndexError()

        return self._data[self._head]

    def is_empty(self) -> bool:
        """Пустая ли очередь."""
        return self._head >= len(self._data)

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data) - self._head
