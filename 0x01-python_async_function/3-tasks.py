#!/usr/bin/env python3
""" The basics of async """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        @max_delay: max delay of wait_random
        Return: asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))
