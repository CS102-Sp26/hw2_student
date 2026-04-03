import pytest
import os
import tempfile
from bounce_hashing import h1, h2, insert, delete, lookup, main


# ─── Helper ───────────────────────────────────────────────────────────────────

def _write_input(lines):
    """Write lines to a temp file and return its path."""
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write("\n".join(lines) + "\n")
    tmp.close()
    return tmp.name


# ─── Hash Function Tests ─────────────────────────────────────────────────────

class TestHashFunctions:
    def test_h1(self):
        assert h1(6, 5) == 1
        assert h1(11, 5) == 1
        assert h1(0, 5) == 0

    def test_h2(self):
        assert h2(6, 5) == 3    # (6//7 + 3) % 5 = (0+3) % 5 = 3
        assert h2(11, 5) == 4   # (11//7 + 3) % 5 = (1+3) % 5 = 4
        assert h2(0, 5) == 3    # (0//7 + 3) % 5 = 3


# ─── Basic Operation Tests ───────────────────────────────────────────────────

class TestBasicOperations:
    def test_insert_into_empty(self):
        t1 = [None] * 5
        t2 = [None] * 5
        insert(6, 5, t1, t2)
        assert t1 == [None, 6, None, None, None]
        assert t2 == [None] * 5

    def test_lookup_found(self):
        t1 = [None] * 5
        t2 = [None] * 5
        insert(3, 5, t1, t2)
        assert lookup(3, 5, t1, t2) is True

    def test_lookup_not_found(self):
        t1 = [None] * 5
        t2 = [None] * 5
        assert lookup(42, 5, t1, t2) is False

    def test_delete(self):
        t1 = [None] * 5
        t2 = [None] * 5
        insert(3, 5, t1, t2)
        delete(3, 5, t1, t2)
        assert lookup(3, 5, t1, t2) is False


# ─── Sample Tests (from the assignment) ──────────────────────────────────────

class TestSamples:
    def test_sample1(self):
        path = _write_input([
            "5 8",
            "INSERT 6", "INSERT 11", "INSERT 16",
            "DELETE 6",
            "LOOKUP 11", "LOOKUP 6",
            "INSERT 3",
            "LOOKUP 3",
        ])
        t1, t2, results = main(path)
        assert t1 == [None, 16, None, 3, None]
        assert t2 == [None, None, None, None, 11]
        assert results == [True, False, True]
        os.unlink(path)

    def test_sample2(self, capsys):
        path = _write_input([
            "5 7",
            "INSERT 0", "INSERT 5", "INSERT 10", "INSERT 15", "INSERT 20",
            "LOOKUP 5", "LOOKUP 10",
        ])
        t1, t2, results = main(path)
        captured = capsys.readouterr()
        assert "Cycle detected! Cannot insert key: 20" in captured.out
        assert t1 == [5, None, None, None, None]
        assert t2 == [15, None, None, 0, 10]
        assert results == [True, True]
        os.unlink(path)
