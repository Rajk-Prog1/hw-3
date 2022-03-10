import pytest
from src.programming_tasks.nested_lists.nested_lists import nested_lists

class TestNestedLists(object):

    def test_1(self):
        assert nested_lists([["Prashant", 32], ["Pallavi", 36], ["Dheeraj", 39], ["Shivam", 40]]) == ["Pallavi"]

    def test_2(self):
        assert nested_lists([["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]) == ["Berry", "Harry"]

    def test_3(self):
        assert nested_lists([["Sona", -25.001], ["Mona", -25.0001], ["Mini", -25.000], ["Rita",-25.0]]) == ["Mona"]