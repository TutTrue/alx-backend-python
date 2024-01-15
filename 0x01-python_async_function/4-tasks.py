#!/usr/bin/env python3
""" The basics of async """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        @n: times to call wait_random
        @max_delay: max delay of wait_random
        Return: list of all delays
    """
    delays: List[asyncio.Future[float]] = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))

    result: List[float] = []
    for delay in asyncio.as_completed(delays):
        result.append(await delay)
    return result
