import pytest
from src.programming_tasks.arithmetic_operators.arithmetic_operators import arithmetic_operators

class TestArithmeticOperators(object):

    def test_1(self):
        assert arithmetic_operators(3, 2) == (5, 1, 6)

    def test_2(self):
        assert arithmetic_operators(6564424525, 323252462) == (6887676987, 6241172063, 2121966389319430550)

