#!/usr/bin/env python3
""" This module contains the function that takes
a tuple and factor and returns a tuple """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ This function takes a tuple and factor and returns a tuple """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
