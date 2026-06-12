import unittest
from app.calculator import suma, resta

class TestCalculator(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
