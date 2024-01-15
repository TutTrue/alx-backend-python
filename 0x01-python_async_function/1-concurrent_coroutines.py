#!/bin/usr/env python3
""" The basics of async """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    li = [await wait_random(max_delay) for _ in range(n)]
    res = []
    for i in asyncio.as_completed(li):
        res.append(await i)
    return res
