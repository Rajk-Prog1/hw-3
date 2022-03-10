import pytest
from src.programming_tasks.loops.loops import loops

class TestLoops(object):

    def test_1(self):
        assert loops(5) == [0, 1, 4, 9, 16]

    def test_2(self):
        assert loops(9) == [0, 1, 4, 9, 16, 25, 36, 49, 64]
