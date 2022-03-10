import pytest
from src.programming_tasks.leap_year.leap_year import leap_year

class TestLeapYear(object):

    def test_1(self):
        assert leap_year(2000) == True

    def test_2(self):
        assert leap_year(2100) == False

    def test_3(self):
        assert leap_year(2400) == True

    def test_4(self):
        assert leap_year(3455) == False

    def test_5(self):
        assert leap_year(1990) == False

    def test_6(self):
        assert leap_year(1992) == True
