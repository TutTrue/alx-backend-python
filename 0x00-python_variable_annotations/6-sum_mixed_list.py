#!/usr/bin/env python3
""" This module sum all the elements of a mixed list """
from typing import Union, List
mixed = Union[int, float]


def sum_mixed_list(mxd_lst: List[mixed]) -> float:
    """ This function sum all the elements of a mixed list """
    return sum(mxd_lst)
