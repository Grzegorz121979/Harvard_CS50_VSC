"""modul solution.py class Solution """
from solution import Solution


solution = Solution()

def test_one() -> None:
    """test function"""
    assert solution.factorial(2) ==  2

def test_two() -> None:
    """test function"""
    assert solution.factorial(6) == 720
    
def test_three() -> None:
    """test function"""
    assert solution.factorial(3) == 6

def test_four() -> None:
    """test function"""
    assert solution.factorial(12) == 479001600

def test_five() -> None:
    """test function"""
    assert solution.factorial(5) == 120
