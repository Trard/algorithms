import pytest
from src.adt.list_queue import ListQueue

def test_enqueue_dequeue_fifo():
    q = ListQueue()
    items = [10, 20, 30, 40]
    for x in items:
        q.enqueue(x)
    assert len(q) == 4
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.dequeue() == 40
    assert q.is_empty()
    assert len(q) == 0

def test_front_peek_does_not_remove():
    q = ListQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1
    assert len(q) == 2
    assert q.dequeue() == 1
    assert q.front() == 2

def test_empty_queue_raises():
    q = ListQueue()
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.front()

def test_len_and_is_empty_with_interleaving():
    q = ListQueue()
    assert q.is_empty()
    q.enqueue(7)
    assert not q.is_empty()
    assert len(q) == 1
    q.enqueue(8)
    assert len(q) == 2
    assert q.dequeue() == 7
    assert len(q) == 1
    assert q.dequeue() == 8
    assert q.is_empty()
    assert len(q) == 0
