import pytest
from exercises.sort import insertion_sort


@pytest.mark.parametrize('problem,expected_answer', [
    ([3, 2, 4, 1], [1, 2, 3, 4]),
    ([5, 7, 4, 8, 1, 2, 6, 3], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([3, 7, 11, 1], [1, 3, 7, 11]),
    ([2], [2]),
    ([3, 4, 4, 2, 3, 2, 2], [2, 2, 2, 3, 3, 4, 4])
])
def test_insertion_sort(problem, expected_answer):
    assert insertion_sort(problem) == expected_answer
