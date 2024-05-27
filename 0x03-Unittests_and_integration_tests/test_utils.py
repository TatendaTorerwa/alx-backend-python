#!/usr/bin/env python3
"""Testing the utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function using parameterized"""
    @parameterized.expand([
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
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_get
            ) -> None:

        """Create a Mock response object with a json method
        that returns test_payload."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        """Call the function with the test URL."""
        result = get_json(test_url)

        """Assert the get method was called once with the test URL."""
        mock_get.assert_called_once_with(test_url)

        """Assert the function returned the expected payload."""
        self.assertEqual(result, test_payload)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

    with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
        test_class = TestClass()
        self.assertEqual(test_class.a_property(), 42)
        self.assertEqual(test_class.a_property(), 42)
        memo_fxn.assert_called_once()
