import pytest
from src.programming_tasks.split_join.split_join import split_join

class TestSplitJoin(object):

    def test_1(self):
        assert split_join("this is a string") == "this-is-a-string"

    def test_2(self):
        assert split_join("quick brown fox jumps over a lazy dog") == "quick-brown-fox-jumps-over-a-lazy-dog"
