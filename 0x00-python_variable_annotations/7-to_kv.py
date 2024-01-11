#!/usr/bin/env python3
""" This module contains the function to_kv """
from typing import Tuple, Union
v_t = Union[int, float]
r_t = Tuple[str, float]


def to_kv(k: str, v: v_t) -> r_t:
    """ This function returns a tuple """
    return (k, v**2)
