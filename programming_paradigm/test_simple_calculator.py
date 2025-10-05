import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADDITION TESTS ----------
    def test_addition(self):
        """Test addition with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 7), 7)

    # ---------- SUBTRACTION TESTS ----------
    def test_subtraction(self):
        """Test subtraction with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ---------- MULTIPLICATION TESTS ----------
    def test_multiplication(self):
        """Test multiplication with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # ---------- DIVISION TESTS ----------
    def test_division(self):
        """Test normal division cases."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
