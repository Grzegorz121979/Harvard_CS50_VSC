"""modul solution.py class Solution """
from solution import Solution


solution = Solution()

def test_one() -> None:
    """test function"""
    assert solution.asc_des_none([4, 3, 2, 1], "Asc") == [1, 2, 3, 4]

def test_two() -> None:
    """test function"""
    assert solution.asc_des_none([7, 8, 11, 66], "Des") == [66, 11, 8, 7]

def test_three() -> None:
    """test function"""
    assert solution.asc_des_none([1, 2, 3, 4], "None") == [1, 2, 3, 4]

def test_four() -> None:
    """test function"""
    assert solution.asc_des_none([4, 3, 2, 1], "Asc") == [1, 2, 3, 4]

def test_five() -> None:
    """test function"""
    assert solution.asc_des_none([1, 0, 1, 0], "Asc") == [0, 0, 1, 1]
    
def test_six() -> None:
    """test function"""
    assert solution.asc_des_none([1, 2, 2, 2, 2, 2, 2], "Des") == [2, 2, 2, 2, 2, 2, 1]

def test_seven() -> None:
    """test function"""
    assert solution.asc_des_none([9, 7, 43, 11, 16, 111, 19], "Asc") == [7, 9, 11, 16, 19, 43, 111]
  