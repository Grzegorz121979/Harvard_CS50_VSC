class Solution:
    """
    Class Solution contain a function with solution of challenges
    """
    def factorial(self, num: int) -> int:
        """
        function that takes an integer and returns the factorial of that integer
        
        Args:
            num (int): 

        Returns:
            int: 
        """
        # num = 5
        # 5 * 4 * 3 * 2 * 1 = 120
        if num == 1:
            return num
        return num * self.factorial(num - 1)
            