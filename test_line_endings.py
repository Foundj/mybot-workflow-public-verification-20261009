"""Immutable acceptance fixture for the isolated GitHub repository."""
import unittest
from line_endings import normalize_line_endings

class LineEndingsContract(unittest.TestCase):
    def test_crlf(self):
        self.assertEqual(normalize_line_endings("a\r\nb\r\n"), "a\nb\n")
    def test_lone_cr(self):
        self.assertEqual(normalize_line_endings("a\rb\r"), "a\nb\n")
    def test_mixed_and_existing_lf(self):
        self.assertEqual(normalize_line_endings("a\r\nb\rc\nd"), "a\nb\nc\nd")
    def test_empty(self):
        self.assertEqual(normalize_line_endings(""), "")
    def test_unicode(self):
        self.assertEqual(normalize_line_endings("你好\r\n世界"), "你好\n世界")
    def test_non_strings_rejected(self):
        for value in (None, 3, [], {}):
            with self.subTest(value=value), self.assertRaises(TypeError):
                normalize_line_endings(value)
