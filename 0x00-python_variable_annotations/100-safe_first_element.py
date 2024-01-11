#!/usr/bin/env python3
""" This module contains a function that returns the first element of a list """
from typing import Sequence, Any, Union
lst_t = Sequence[Any]
r_t = Union[Any, None]


def safe_first_element(lst: lst_t) -> r_t:
    """ This function returns the first element of a list """
    if lst:
        return lst[0]
    else:
        return None
