#!/usr/bin/env python3
"""Complex types - string and int/float to tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is the string k and the second
    is the square of v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value, which can be either
        an int or a float.

    Returns:
        Tuple[str, float]: A tuple.
    """
    return (k, v ** 2)
