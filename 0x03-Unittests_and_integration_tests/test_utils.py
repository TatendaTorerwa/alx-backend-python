#!/usr/bin/env/python3
"""Testing the utils module."""

import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)

Class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function
    using the parameterized decorator.
    """

    @@parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)
