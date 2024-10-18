import unittest
from src.prueba1 import suma

class TestPrueba1(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
