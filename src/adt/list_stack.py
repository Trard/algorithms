"""
Стек на списке
"""
class ListStack:
    def __init__(self):
        self._data = []
        self._min_stack = []

    def push(self, x: int):
        """Поместить x в стек."""
        self._data.append(x)

        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> int:
        """Удалить и вернуть верхний элемент. Бросает IndexError, если стек пуст."""
        if not self._data:
            raise IndexError()

        val = self._data.pop()

        if self._min_stack and val == self._min_stack[-1]:
            self._min_stack.pop()

        return val

    def peek(self) -> int:
        """Вернуть верхний элемент без удаления. Бросает IndexError, если стек пуст."""

        if not self._data:
            raise IndexError()

        return self._data[-1]

    def is_empty(self) -> bool:
        """Пуст ли стек."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)

    def min(self) -> int:
        """Текущий минимум в стеке. Бросает IndexError, если стек пуст."""
        if not self._min_stack:
            raise IndexError()

        return self._min_stack[-1]
