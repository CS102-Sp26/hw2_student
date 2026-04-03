import pytest

from bucket_util import *
from lifo_bucket import main

@pytest.mark.parametrize(
    "fname, expected",
    [
        ("lifo_case01.txt", "[[0, 2, 3, 1]]"),
        ("lifo_case02.txt", "[[1, 2, 3, 4, 0]]"),
        ("lifo_case03.txt", "[[2, 1, 0], [3, 5, 4]]"),
        ("lifo_case04.txt", "[[3, 6, 5, 4], [1, 2, 0]]"),
        ("lifo_case05.txt", "[[6, 7, 3, 4, 5], [1, 2, 0]]"),
        ("lifo_case06.txt", "[[0, 2, 1], [3, 4], [5], [6]]"),
        ("lifo_case07.txt", "[[7, 6], [1, 2, 0], [3, 5, 4]]"),
        ("lifo_case08.txt", "[[5, 4], [1, 3, 2, 0], [6, 7]]"),
        ("lifo_case09.txt", "[[1, 3, 2, 0], [4, 6, 5], [7], [8]]"),
        ("lifo_case10.txt", "[[0, 4, 3, 2, 1], [5], [6], [7], [8], [9]]"),
    ]
)
def test_lifo_bucket(fname, expected):
    got = main("inputs/" + ALGOS[LIFO] + "/" + fname)
    assert got == expected
