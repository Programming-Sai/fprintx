# tests/test_fprintx.py

import unittest
import io
import contextlib
from fprintx.core import printx

class TestPrintx(unittest.TestCase):
    def capture_print(self, *args, **kwargs):
        """Helper function to capture printed output."""
        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            printx(*args, **kwargs)
        return captured_output.getvalue()
    
    def test_default_formatting(self):
        # With no custom widths, alignments, or styles, it should use defaults.
        result = self.capture_print("Hello", "World")
        # Default widths become the maximum length among args; here both are 5.
        # They are left-aligned by default.
        expected = "Hello World\n"
        self.assertEqual(result, expected)
    
    def test_custom_widths(self):
        # Test custom widths with two arguments.
        result = self.capture_print("Hi", "World", widths=[10, 15])
        # "Hi" padded to 10 chars and "World" to 15 chars (left-aligned by default).
        expected = "Hi         World          \n"
        self.assertEqual(result, expected)
    
    def test_custom_alignments(self):
        # Test custom alignments.
        result = self.capture_print("Test", "Align", alignments=['>', '^'], widths=[5, 5])
        # "Test" right-aligned in a width of 5, and "Align" centered in a width of 5.
        expected = " Test Align\n"  # "Test" becomes " Test" and "Align" stays as "Align"
        self.assertEqual(result, expected)
    
    def test_custom_styles(self):
        # Test custom styles for bold.
        result = self.capture_print("Bold", styles=['bold'], widths=[4])
        # ANSI escape sequence for bold should be in the output.
        self.assertIn("\033[1mBold\033[0m", result)
    
    def test_truncate(self):
        # Test truncation when value is too long.
        # With widths=[10] and truncate=True, if the value length is > width + 10,
        # it truncates to the first 10 characters and adds '...'.
        long_text = "LongTextValueExceeding"
        result = printx(long_text, widths=[10], truncate=True, return_as_str=True)
        # Expected: first 10 characters of long_text plus '...'
        expected = long_text[:10] + "..."
        self.assertEqual(result.strip(), expected)
    
    def test_list_shorter_than_args(self):
        # When the provided widths list is shorter than number of args,
        # the last value is repeated.
        result = self.capture_print("One", "Two", "Three", widths=[5])
        # Expected widths become [5, 5, 5] for each argument.
        # "One" -> "One  ", "Two" -> "Two  ", "Three" -> "Three" (exactly 5 chars, no truncation)
        expected = "One   Two   Three\n"
        self.assertEqual(result, expected)
    
    def test_return_as_str(self):
        # Test that the function returns the string when return_as_str is True.
        result = printx("Test", return_as_str=True)
        self.assertEqual(result.strip(), "Test")
    
    def test_mixed_types(self):
        # Test that mixed types (strings, numbers, floats) are handled correctly.
        result = self.capture_print("Number", 123, 45.67, widths=[7, 7, 7])
        # Convert each value to string and format it in a 7-character wide field.
        expected_parts = ["Number", "123", "45.67"]
        for part in expected_parts:
            self.assertIn(part, result)
    
if __name__ == '__main__':
    unittest.main()
