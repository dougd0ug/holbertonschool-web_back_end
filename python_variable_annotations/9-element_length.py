#!/usr/bin/env python3
"""
return vlaue with type
"""
from typing import Sequence, Tuple, List

def element_length(lst: Sequence[str]) -> List[Tuple[str, int]]:
    """
    return value with type
    """
    return [(i, len(i)) for i in lst]
