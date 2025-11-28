import pytest
from src.adt.list_stack import ListStack

def test_push_pop_lifo():
    s = ListStack()
    elems = [1, 2, 3, 4]
    for e in elems:
        s.push(e)
    assert len(s) == 4
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    assert len(s) == 0

def test_peek_does_not_remove_and_raises_on_empty():
    s = ListStack()
    with pytest.raises(IndexError):
        s.peek()
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert len(s) == 2
    assert s.pop() == 20
    assert s.peek() == 10

def test_empty_pop_and_min_raise():
    s = ListStack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.min()
    s.push(5)
    assert s.min() == 5
    assert s.pop() == 5
    with pytest.raises(IndexError):
        s.min()

def test_min_updates_with_duplicates():
    s = ListStack()
    s.push(3)
    s.push(1)
    s.push(1)
    s.push(2)
    assert s.min() == 1
    assert s.pop() == 2
    assert s.min() == 1
    assert s.pop() == 1
    assert s.min() == 1
    assert s.pop() == 1
    assert s.min() == 3
    assert s.pop() == 3
    assert s.is_empty()

def test_len_and_is_empty_interleaving():
    s = ListStack()
    assert s.is_empty()
    s.push(7)
    assert not s.is_empty()
    assert len(s) == 1
    s.push(8)
    assert len(s) == 2
    assert s.pop() == 8
    assert len(s) == 1
    assert s.pop() == 7
    assert s.is_empty()
    assert len(s) == 0

def test_many_operations_min_stability():
    s = ListStack()
    expected_stack = []
    expected_min_stack = []

    import random
    random.seed(0)

    for i in range(200):
        op = random.choice(["push", "pop"])
        if op == "push" or not expected_stack:
            val = random.randint(-50, 50)
            s.push(val)
            expected_stack.append(val)
            if not expected_min_stack or val <= expected_min_stack[-1]:
                expected_min_stack.append(val)
        else:
            popped = s.pop()
            exp = expected_stack.pop()
            assert popped == exp
            if expected_min_stack and exp == expected_min_stack[-1]:
                expected_min_stack.pop()

        assert len(s) == len(expected_stack)
        assert s.is_empty() == (len(expected_stack) == 0)
        if expected_stack:
            assert s.peek() == expected_stack[-1]
            assert s.min() == expected_min_stack[-1]
        else:
            with pytest.raises(IndexError):
                s.min()
            with pytest.raises(IndexError):
                s.peek()
