import random
import functools
import pytest

from src.sort.counting_sort import counting_sort
from src.sort.quick_sort import quick_sort
from src.sort.heap_sort import heap_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.bubble_sort import bubble_sort
from src.sort.radix_sort import radix_sort
# from src.benchmark.benchmark import benchmark_sorts  # not used by tests

# ---- Provide your sorts here (can be functions, partials, or (name, fn) tuples) ----
RAW_SORT_FUNCS = [
    bubble_sort,
    counting_sort,
    radix_sort,
    heap_sort,
    quick_sort,
    functools.partial(bucket_sort, heap_sort),
    # you can also use ("my_name", my_fn) tuples if you prefer explicit ids
]

# ---- Normalize into (name, fn) pairs for pytest paramization ----
def _get_name_for_callable(fn):
    # partial: use underlying function name with '_partial' suffix
    if isinstance(fn, functools.partial):
        base = getattr(fn.func, "__name__", repr(fn.func))
        return f"{base}_partial"
    # normal callable
    name = getattr(fn, "__name__", None)
    if name:
        return name
    # fallback
    return repr(fn)

SORT_FUNCS = []
for item in RAW_SORT_FUNCS:
    if isinstance(item, tuple) and len(item) == 2:
        SORT_FUNCS.append((str(item[0]), item[1]))
    else:
        SORT_FUNCS.append((_get_name_for_callable(item), item))


# ---- Pytest fixture to parametrize sorts ----
@pytest.fixture(params=SORT_FUNCS, ids=[name for name, _ in SORT_FUNCS])
def sorter(request):
    """Yields a tuple (name, fn) for each discovered sort function."""
    return request.param  # (name, fn)


# ---- Helpers: get result list in a way that tolerates in-place sorts ----
def _as_list_result(fn, inp):
    """
    Call fn on a *copy* of inp (so tests can reason about original).
    Returns a tuple (result_list, returned_object, mutated_input_copy).
      - result_list: the final sorted list (Python list)
      - returned_object: the raw object returned by the function (could be None)
      - mutated_input_copy: the copy we passed into fn after the call (useful to detect mutation)
    """
    # work on a copy to avoid mutating caller's list
    inp_copy = inp.copy()
    returned = fn(inp_copy)

    if returned is None:
        # convention: in-place sort that returns None -> use mutated inp_copy
        result_list = list(inp_copy)
        returned_obj = None
    else:
        # function returned something. If it returned the same object we passed, use that;
        # otherwise convert returned to list (supports generators/iterables).
        if returned is inp_copy:
            result_list = list(returned)
            returned_obj = returned
        else:
            # convert returned to list in case it's not a list already
            result_list = list(returned)
            returned_obj = returned

    return result_list, returned_obj, inp_copy


# ---- Assertions helper ----
def _assert_sorted_equal_to_python_sorted(result, original):
    assert result == sorted(original)


# ---- Tests ----
def test_empty_and_single(sorter):
    name, fn = sorter

    original = []
    res_list, returned_obj, mutated = _as_list_result(fn, original)
    _assert_sorted_equal_to_python_sorted(res_list, original)

    original = [42]
    res_list, returned_obj, mutated = _as_list_result(fn, original)
    _assert_sorted_equal_to_python_sorted(res_list, original)


def test_sorted_and_reverse(sorter):
    name, fn = sorter

    original = [1, 2, 3, 4, 5]
    res_list, *_ = _as_list_result(fn, original)
    _assert_sorted_equal_to_python_sorted(res_list, original)

    original = [5, 4, 3, 2, 1]
    res_list, *_ = _as_list_result(fn, original)
    _assert_sorted_equal_to_python_sorted(res_list, original)


def test_duplicates_and_negatives(sorter):
    name, fn = sorter

    original = [3, -1, 2, -1, 3, 0]
    res_list, *_ = _as_list_result(fn, original)
    _assert_sorted_equal_to_python_sorted(res_list, original)


def test_input_mutation_behavior(sorter):
    name, fn = sorter

    original = [random.randint(-50, 50) for _ in range(30)]
    copy_before = original.copy()

    # check mutation behavior by calling fn on a fresh copy and observing return / mutated copy
    res_list, returned_obj, mutated_copy = _as_list_result(fn, original)

    assert res_list == sorted(copy_before)

    # if the function returned the *same* object we passed, it likely mutated in-place
    if returned_obj is mutated_copy:
        assert mutated_copy == res_list
    else:
        # returned different object or None -> ensure original (copy_before) was unchanged
        # (note: in _as_list_result we always called fn on inp_copy so the original `original` is untouched)
        assert copy_before == original


def test_random_lists(sorter):
    name, fn = sorter

    random.seed(0)
    for size in (10, 50, min(100, 500)):
        lst = [random.randint(-1000, 1000) for _ in range(size)]
        original = lst.copy()
        res_list, *_ = _as_list_result(fn, original)
        _assert_sorted_equal_to_python_sorted(res_list, original)
