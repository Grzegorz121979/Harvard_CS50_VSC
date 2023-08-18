"""modul solution.py class Solution """
from solution import Solution


solution = Solution()

def test_one() -> None:
    """test function"""
    assert solution.binary(100) == '1100100'

def test_two() -> None:
    """test function"""
    assert solution.binary(1) == '1'

def test_three() -> None:
    """test function"""
    assert solution.binary(0) == '0'

def test_four() -> None:
    """test function"""
    assert solution.binary(69) == '1000101'

def test_five() -> None:
    """test function"""
    assert solution.binary(1023) == '1111111111'

def test_six() -> None:
    """test function"""
    assert solution.binary(511) == '111111111'

def test_seven() -> None:
    """test function"""
    assert solution.binary(666) == '1010011010'

def test_eight() -> None:
    """test function"""
    assert solution.binary(123) == '1111011'
