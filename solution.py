from math import floor as fl


class Solution:
    """
    Class Solution contain a function with solution of challenges
    """
    def binary(self, decimal: int) -> str:
        """
        function that returns a base-2 (binary) representation of a base-10 (decimal)

        Args:
            decimal (int): decimal number

        Returns:
            str: binary representation
        """
        if decimal < 1:
            return ''
        return self.binary(fl(decimal / 2)) + str(decimal % 2)
            