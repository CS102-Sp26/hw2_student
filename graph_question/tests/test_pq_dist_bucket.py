import pytest

from bucket_util import *
from pq_dist_bucket import main

@pytest.mark.parametrize(
    "fname, expected",
    [
        ("pq_dist_case01.txt", "[[0, 1, 2, 3]]"),
        ("pq_dist_case02.txt", "[[2, 3, 0, 1]]"),
        ("pq_dist_case03.txt", "[[1, 2, 0, 3, 4]]"),
        ("pq_dist_case04.txt", "[[3, 4, 1, 2, 0]]"),
        ("pq_dist_case05.txt", "[[0, 1, 3, 2, 4, 5]]"),
        ("pq_dist_case06.txt", "[[4, 5, 0, 2, 3, 1]]"),
        ("pq_dist_case07.txt", "[[2, 1, 3, 0, 4, 5, 6]]"),
        ("pq_dist_case08.txt", "[[5, 4, 2, 6, 1, 3, 0]]"),
        ("pq_dist_case09.txt", "[[0, 1, 2, 3, 4, 5, 6, 7]]"),
        ("pq_dist_case10.txt", "[[6, 3, 7, 5, 2, 4, 0, 1]]"),
    ]
)
def test_pq_dist_bucket(fname, expected):
    got = main("inputs/" + ALGOS[PQ_DIST] + "/" + fname)
    assert got == expected
