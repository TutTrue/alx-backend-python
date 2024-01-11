#!/usr/bin/env python3
""" This module sum all the elements of a mixed list """
import typing
mixed = typing.Union[int, float]


def sum_mixed_list(mxd_lst: list[mixed]) -> float:
    """ This function sum all the elements of a mixed list """
    return sum(mxd_lst)
