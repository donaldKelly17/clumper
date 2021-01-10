from clumper import Clumper
import pytest


@pytest.mark.parametrize("n,expected", [(0, 0), (5, 5), (10, 10), (26, 26), (1000, 26)])
def test_headtail_size(base_clumper, n, expected):
    assert len(base_clumper.head(n)) == expected
    assert len(base_clumper.tail(n)) == expected


@pytest.mark.parametrize("idx", [i for i in range(1, 26)])
def test_can_collect_head(base_clumper, idx):
    collected = base_clumper.head(idx).collect()
    assert collected[-1]["i"] == idx - 1


def test_can_collect_tail():
    data = [{"i": i} for i in range(10)]
    c = Clumper(data).tail(1)
    collected = c.collect()
    assert collected[0]["i"] == 9
