#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> List[float]:
    """
        @max_delay: max delay of wait_random
        Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
