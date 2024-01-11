#!/usr/bin/env python3
""" This module contains the make_multiplier function """
from typing import Callable
r_t = Callable[[float], float]


def make_multiplier(multiplier: float) -> r_t:
    """ This function returns a function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """ This function multiplies a float by multiplier """
        return n * multiplier
    return multiply
