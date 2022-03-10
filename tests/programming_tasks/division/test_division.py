import pytest
from src.programming_tasks.division.division import division

class TestDivision(object):

    def test_1(self):
        assert division(4, 3) == (1, 4/3)

    def test_2(self):
        assert division(6564424525, 323252462) == (20, 6564424525/323252462)
