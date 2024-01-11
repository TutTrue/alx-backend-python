#!/usr/bin/env python3
""" This module contains a type-annotated function safely_get_value """
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')
default_t = Union[T, None]
r_t = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: default_t = None) -> r_t:
    """ This function returns the value of a key safely """
    if key in dct:
        return dct[key]
    else:
        return default
