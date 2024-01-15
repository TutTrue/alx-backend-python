#!/bin/usr/env python3
""" The basics of async """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ Waits for a random delay between 0 and max_delay """
    list_delays = []
    for i in range(n):
        list_delays.append(await wait_random(max_delay))
    return sorted(list_delays)
