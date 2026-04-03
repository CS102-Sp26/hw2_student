import pytest
from fast_fibonacci import main

@pytest.mark.parametrize(
    "fname, expected",
    [
        ("hw_case1.txt", "0"),
        ("hw_case2.txt", "1"),
        ("hw_case3.txt", "5"),
        ("hw_case4.txt", "55"),
        ("hw_case5.txt", "6765"),
        ("hw_case6.txt", "832040"),
    ],
)
def test_hwupdated_cases(fname, expected):
    got = main("inputs/" + fname)
    assert got == expected
