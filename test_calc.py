import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(20, 9)
        self.assertEqual(result, 29)

    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()