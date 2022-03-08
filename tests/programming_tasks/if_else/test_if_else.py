import pytest
from src.programming_tasks.if_else.if_else import if_else

class TestIfElse(object):

    def test_1(self):
        assert if_else(3) == "Weird"

    def test_2(self):
        assert if_else(24) == "Not Weird"

    def test_3(self):
        assert if_else(4) == "Not Weird"

    def test_4(self):
        assert if_else(18) == "Weird"

    def test_5(self):
        assert if_else(29) == "Weird"

    def test_6(self):
        assert if_else(5) == "Weird"    

    def test_7(self):
        assert if_else(100) == "Not Weird"  

    def test_8(self):
        assert if_else(20) == "Weird"  