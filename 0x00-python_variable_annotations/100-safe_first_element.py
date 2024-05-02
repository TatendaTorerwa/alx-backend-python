#!/usr/bin/env python3
"""Duck typing - first element of a sequence."""

from typing import Iterable, Any, Union


def safe_first_element(lst: Iterable[Any]) -> Union[Any, None]:
    """
    Return the first element of the iterable
    safely, or None if the iterable is empty.

    Args:
        lst (Iterable[Any]): The input iterable.

    Returns:
        Union[Any, None]: The first element of
        the iterable, or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
