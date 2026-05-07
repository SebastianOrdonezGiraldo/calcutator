import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    
    def setUp(self):
        self.calc = Calculator()

    def test_suma(self):
        # Ahora self.calc ya existirá
        self.assertEqual(self.calc.sumar(5, 5), 10)

    def test_resta(self):
        self.assertEqual(self.calc.restar(10, 5), 5)

    def test_division(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
