"""modul solution.py class Solution """
from solution import Solution


solution = Solution()

def test_one():
    assert solution.correct_signs("3 < 7 < 11") is True


def test_two():
    assert solution.correct_signs("13 > 44 > 33 > 1") is False


def test_three():
    assert solution.correct_signs("1 < 2 < 6 < 9 > 3") is True


def test_four():
    assert solution.correct_signs("4 > 3 > 2 > 1") is True


def test_five():
    assert solution.correct_signs("5 < 7 > 1") is True


def test_six():
    assert solution.correct_signs("5 > 7 > 1") is False


def test_seven():
    assert solution.correct_signs("9 < 9") is False
