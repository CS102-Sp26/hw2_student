import pytest

from bucket_util import *
import basic_bucket
import fifo_bucket
import lifo_bucket
import pq_edge_bucket


@pytest.mark.parametrize(
    "fname, expected",
    [
        ("basic_case01.txt", "[4]"),
        ("basic_case02.txt", "[5]"),
        ("basic_case03.txt", "[3, 3]"),
        ("basic_case04.txt", "[4, 3]"),
        ("basic_case05.txt", "[5, 3]"),
        ("basic_case06.txt", "[3, 2, 1, 1]"),
        ("basic_case07.txt", "[2, 3, 3]"),
        ("basic_case08.txt", "[2, 4, 2]"),
        ("basic_case09.txt", "[4, 3, 1, 1]"),
        ("basic_case10.txt", "[5, 1, 1, 1, 1, 1]"),
    ]
)
def test_basic_bucket(fname, expected):
    got = basic_bucket.main("inputs/" + ALGOS[BASIC] + "/" + fname)
    assert got == expected


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
    got = fifo_bucket.main("inputs/" + ALGOS[FIFO] + "/" + fname)
    assert got == expected

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
    got = lifo_bucket.main("inputs/" + ALGOS[LIFO] + "/" + fname)
    assert got == expected


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
    got = pq_edge_bucket.main("inputs/" + ALGOS[PQ_EDGE] + "/" + fname)
    assert got == expected
