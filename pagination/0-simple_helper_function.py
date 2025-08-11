#!/usr/bin/env python3
"""
fonction to help for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    calculate the start and the end of a pagination
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
