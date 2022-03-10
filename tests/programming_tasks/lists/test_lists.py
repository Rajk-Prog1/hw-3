import pytest
from src.programming_tasks.lists.lists import lists

class TestLists(object):

    def test_1(self):
        assert lists(["insert 0 5", "insert 1 10", "insert 0 6", "remove 6", "append 9", "append 1", "sort", "pop", "reverse", "return"]) == [9, 5, 1]

    def test_2(self):
        assert lists(["append 1","append 6","append 10","append 8","append 9"
                    ,"append 2","append 12","append 7","append 3","append 5"
                    ,"insert 8 66","insert 1 30","insert 6 75","insert 4 44","insert 9 67","insert 2 44"
                    ,"insert 9 21","insert 8 87","insert 1 75","insert 1 48","reverse"
                    ,"sort","append 2","append 5","remove 2","return"]) == [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
