#!/usr/bin/env python3
from typing import Union, Tuple
"""
square with a tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    square with a tuple
    """
    return (k, float(v ** 2))
