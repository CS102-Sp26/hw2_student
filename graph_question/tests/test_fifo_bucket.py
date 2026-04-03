import pytest

from bucket_util import *
from fifo_bucket import main

@pytest.mark.parametrize(
    "fname, expected",
    [
        ("fifo_case01.txt", "[[0, 1, 2, 3]]"),
        ("fifo_case02.txt", "[[1, 0, 2, 3, 4]]"),
        ("fifo_case03.txt", "[[2, 0, 1], [3, 4, 5]]"),
        ("fifo_case04.txt", "[[3, 4, 6, 5], [1, 0, 2]]"),
        ("fifo_case05.txt", "[[6, 5, 7, 4, 3], [1, 0, 2]]"),
        ("fifo_case06.txt", "[[0, 1, 2], [3, 4], [5], [6]]"),
        ("fifo_case07.txt", "[[7, 6], [1, 0, 2], [3, 4, 5]]"),
        ("fifo_case08.txt", "[[5, 4], [1, 0, 2, 3], [6, 7]]"),
        ("fifo_case09.txt", "[[1, 0, 2, 3], [4, 5, 6], [7], [8]]"),
        ("fifo_case10.txt", "[[0, 1, 2, 3, 4], [5], [6], [7], [8], [9]]"),
    ]
)
def test_fifo_bucket(fname, expected):
    got = main("inputs/" + ALGOS[FIFO] + "/" + fname)
    assert got == expected
