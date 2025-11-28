import pytest
from src.functions.factorial_recursive import factorial_recursive
from src.functions.fibo_recursive import fibo_recursive

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
    (10, 3628800),
])
def test_factorial_values(n, expected):
    factorial_recursive.cache_clear()
    assert factorial_recursive(n) == expected

def test_factorial_negative_raises_recursionerror():
    factorial_recursive.cache_clear()
    with pytest.raises(RecursionError):
        factorial_recursive(-1)

def test_factorial_memoization_hits_increase():
    factorial_recursive.cache_clear()
    info_before = factorial_recursive.cache_info().hits

    factorial_recursive(8)
    factorial_recursive(8)

    info_after = factorial_recursive.cache_info().hits
    assert info_after >= info_before + 1, "Expected cache hits to increase after repeated call"


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (10, 34),
])
def test_fibo_values(n, expected):
    fibo_recursive.cache_clear()
    assert fibo_recursive(n) == expected

def test_fibo_negative_returns_zero():
    fibo_recursive.cache_clear()
    assert fibo_recursive(-10) == 0

def test_fibo_memoization_hits_increase():
    fibo_recursive.cache_clear()
    info_before = fibo_recursive.cache_info().hits

    fibo_recursive(12)
    fibo_recursive(12)

    info_after = fibo_recursive.cache_info().hits
    assert info_after >= info_before + 1, "Expected cache hits to increase after repeated call"
