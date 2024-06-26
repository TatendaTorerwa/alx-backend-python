#!/usr/bin/env python3
"""Complex types - list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list ([List[float]): The input list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """

    return sum(input_list)
