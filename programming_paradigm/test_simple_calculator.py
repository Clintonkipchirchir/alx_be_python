import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, 2), 0)
        self.assertEqual(self.calc.add(10, 2), 12)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(21, 2), 19)
        self.assertEqual(self.calc.subtract(10, 2), 8)
    
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(-14, 2), -7)
        self.assertEqual(self.calc.divide(9, 4), 2.25)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(10, 0), 0)
    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(0, 12),0 )
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(11, 2), 22)
        self.assertEqual(self.calc.multiply(10, 2), 20)
    