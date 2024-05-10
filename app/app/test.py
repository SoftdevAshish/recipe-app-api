"""
Test Calc file some functionality
Simple Test Case
"""

from django.test import SimpleTestCase
from app import calc


class CalcTestCase(SimpleTestCase):
    """Test the Calc functionality."""

    def test_add_numbers(self):
        """Test the addition of two numbers."""
        result = calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """Test the subtraction of two numbers."""
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)
