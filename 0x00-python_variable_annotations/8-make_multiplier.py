#!/usr/bin/env python3
"""Complex types - functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.
    Args:
        multiplier (float): The multiplier to be used in the created function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of the input float and the multiplier.
    """

    def multiplier_function(x: float) -> float:
        """
        Inner function that multiplies a float by the given multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The product of the input float and the multiplier.
        """

        return x * multiplier

    return multiplier_function
