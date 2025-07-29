#!/usr/bin/env python3
"""
async chrono
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n x wait_random
    """
    results = []
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for i in asyncio.as_completed(task):
        result = await i
        results.append(result)

    return result
