#!/bin/usr/env python3
""" The basics of async """
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    return [await wait_random(max_delay) for _ in range(n)]
