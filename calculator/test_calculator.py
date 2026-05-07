import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_suma(self):
        calc = Calculator()
        self.assertEqual(calc.sumar(5, 5), 10)

    def test_resta(self):
        calc = Calculator()
        self.assertEqual(calc.restar(10, 5), 5)

if __name__ == '__main__':
    unittest.main()