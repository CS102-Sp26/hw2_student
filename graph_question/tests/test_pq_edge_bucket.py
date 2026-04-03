import pytest

from bucket_util import *
from pq_edge_bucket import main

@pytest.mark.parametrize(
    "fname, expected",
    [
        ("pq_edge_case01.txt", "[[0, 1, 2, 3]]"),
        ("pq_edge_case02.txt", "[[2, 3, 0, 1]]"),
        ("pq_edge_case03.txt", "[[1, 2, 0, 3, 4]]"),
        ("pq_edge_case04.txt", "[[3, 4, 1, 0, 2]]"),
        ("pq_edge_case05.txt", "[[0, 1, 3, 4, 2, 5]]"),
        ("pq_edge_case06.txt", "[[4, 5, 0, 2, 3, 1]]"),
        ("pq_edge_case07.txt", "[[2, 1, 0, 3, 4, 5, 6]]"),
        ("pq_edge_case08.txt", "[[5, 4, 2, 1, 6, 3, 0]]"),
        ("pq_edge_case09.txt", "[[0, 1, 2, 3, 4, 5, 6, 7]]"),
        ("pq_edge_case10.txt", "[[6, 3, 2, 7, 1, 5, 4, 0]]"),
    ]
)

def test_pq_edge_bucket(fname, expected):
    got = main("inputs/" + ALGOS[PQ_EDGE] + "/" + fname)
    assert got == expected
