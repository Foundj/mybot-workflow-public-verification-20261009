import unittest
from slug import normalize_slug
class SlugContract(unittest.TestCase):
    def test_lowercases_and_collapses_whitespace(self):
        self.assertEqual(normalize_slug("  HeLLo   WORLD  "), "hello-world")
    def test_empty_value(self):
        self.assertEqual(normalize_slug(" \t\n "), "")
    def test_non_string_rejected(self):
        for value in (None, 3, [], {}):
            with self.assertRaises(TypeError):
                normalize_slug(value)
