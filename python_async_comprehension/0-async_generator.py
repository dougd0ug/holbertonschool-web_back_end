#!/usr/bin/env python3
import asyncio
import random
"""
create a rancom loop 10 times
"""


async def async_generator():
    """
    create a random loop 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
