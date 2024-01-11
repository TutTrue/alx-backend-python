#!/usr/bin/env python3
""" This module have a function takes a list of strings and
returns a list of tuples """
from typing import List, Iterable, Sequence, Tuple
lst_t = Iterable[Sequence]
r_t = List[Tuple[Sequence, int]]


def element_length(lst: lst_t) -> r_t:
    """ This function returns a tuple """
    return [(i, len(i)) for i in lst]
