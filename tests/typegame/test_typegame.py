import pytest
import re

def get_answer(num_question):
    
    with open("src/typegame/typegame.md", "r") as file:
        text = file.read()
    answers = re.findall(r"Answer:.*\n", text)

    return answers[num_question - 1].replace("Answer:", "").strip().lower()
    

class TestTypegame(object):

    def test_1(self):
        assert get_answer(1) == "d"

    def test_2(self):
        assert get_answer(2) == "c"

    def test_3(self):
        assert get_answer(3) == "e"

    def test_4(self):
        assert get_answer(4) == "a"

    def test_5(self):
        assert get_answer(5) == "a"
    
    def test_6(self):
        assert get_answer(6) == "c"

    def test_7(self):
        assert get_answer(7) == "e"

    def test_8(self):
        assert get_answer(8) == "b"

    def test_9(self):
        assert get_answer(9) == "d"

    def test_10(self):
        assert get_answer(5) == "b"

    def test_11(self):
        assert get_answer(5) == "c"

    def test_12(self):
        assert get_answer(5) == "e"

    def test_13(self):
        assert get_answer(5) == "d"

    def test_14(self):
        assert get_answer(5) == "d"

    def test_15(self):
        assert get_answer(5) == "a"

    def test_16(self):
        assert get_answer(5) == "b"

    def test_17(self):
        assert get_answer(5) == "a"

    def test_18(self):
        assert get_answer(5) == "a"

    def test_19(self):
        assert get_answer(5) == "b"

    def test_20(self):
        assert get_answer(5) == "c"

    def test_21(self):
        assert get_answer(5) == "d"

    def test_22(self):
        assert get_answer(5) == "b"

    def test_23(self):
        assert get_answer(5) == "c"

    def test_24(self):
        assert get_answer(5) == "e"

    def test_25(self):
        assert get_answer(5) == "a"

    def test_26(self):
        assert get_answer(5) == "e"

    def test_27(self):
        assert get_answer(5) == "b"

    def test_28(self):
        assert get_answer(5) == "d"

    def test_29(self):
        assert get_answer(5) == "e"

    def test_30(self):
        assert get_answer(5) == "a"

    def test_31(self):
        assert get_answer(5) == "b"

    def test_32(self):
        assert get_answer(5) == "d"

    def test_33(self):
        assert get_answer(5) == "c"

    def test_34(self):
        assert get_answer(5) == "a"

    def test_35(self):
        assert get_answer(5) == "c"

    def test_36(self):
        assert get_answer(5) == "b"
