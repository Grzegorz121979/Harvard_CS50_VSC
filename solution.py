class Solution:
    """
    Class Solution contain a function with solution of challenges
    """
    def asc_des_none(self, lst: list[int], s: str) -> list[int] | None:
        """_summary_

        Args:
            lst (list[int]): _description_
            s (str): _description_

        Returns:
            list[int] | None: _description_
        """
        sort_list: dict[str, list[int]] = {
            'Asc': quick_sort_asc(lst),
            'Des': quick_sort_dsc(lst),
            'None': lst
        }

        return sort_list.get(s)


def quick_sort_asc(lst: list[int]) -> list[int]:
    """_summary_

    Args:
        lst (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    if len(lst) < 2:
        return lst
    pivot: int = lst[0]
    less: list[int] = [i for i in lst[1:] if i <= pivot]
    greater: list[int] = [i for i in lst[1:] if i > pivot]

    return quick_sort_asc(less) + [pivot] + quick_sort_asc(greater)


def quick_sort_dsc(lst: list[int]) -> list[int]:
    """_summary_

    Args:
        lst (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    if len(lst) < 2:
        return lst
    pivot: int = lst[0]
    less: list[int] = [i for i in lst[1:] if i <= pivot]
    greater: list[int] = [i for i in lst[1:] if i > pivot]

    return quick_sort_dsc(greater) + [pivot] + quick_sort_dsc(less)
    