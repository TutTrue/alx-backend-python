#!/bin/usr/env python3
""" The basics of async """
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> list:
    """ Waits for a random delay between 0 and max_delay """
    return sorted([await wait_random(max_delay) for _ in range(n)])
