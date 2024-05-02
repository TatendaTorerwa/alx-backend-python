#!/usr/bin/env python3
"""Let's duck type an iterable object."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the list and return
    a list of tuples
    where each tuple contains an element from the input list and its length.

    Args:
        lst (Iterable[Sequence])

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains an element from the input list
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
