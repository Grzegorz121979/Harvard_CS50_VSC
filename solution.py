class Solution:
    """
    Class Solution contain a function with solution of challenges
    """
    def correct_signs(self, txt: str) -> bool:
        """_summary_

        Args:
            txt (str): _description_

        Returns:
            bool: _description_
        """
        lst = txt.split(' ')

        for i in range(len(lst) - 1):
            if lst[i + 1] == '<':
                if int(lst[i]) < int(lst[i + 2]):
                    pass
                else:
                    return False
            if lst[i + 1] == '>':
                if int(lst[i]) > int(lst[i + 2]):
                    pass
                else:
                    return False
        return True
