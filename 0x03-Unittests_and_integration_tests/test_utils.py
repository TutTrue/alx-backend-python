#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import MagicMock, patch, Mock



class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """Test get_json"""
        from utils import get_json
        from unittest.mock import patch
        import requests

        with patch("requests.get") as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize"""

    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """Return 42"""
                return 42

            @memoize
            def a_property(self):
                """Return 42"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 10

            instance_of_test_class = TestClass()
            res = instance_of_test_class.a_property
            self.assertEqual(instance_of_test_class.a_property, res)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
