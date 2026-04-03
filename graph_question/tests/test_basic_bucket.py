import pytest

from bucket_util import *
from basic_bucket import main

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
    got = main("inputs/" + ALGOS[BASIC] + "/" + fname)
    assert got == expected
