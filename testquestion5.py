import unittest
from question5 import ocurrenceCalc


class testq5(unittest.TestCase):
    def test_c1(self):
        self.assertIn(1, ocurrenceCalc(6))

    def test_c2(self):
        self.assertListEqual(ocurrenceCalc(3), [1, 2, 2, 3, 3, 3])

    def test_c3(self):
        self.assertNotEqual(ocurrenceCalc(3), [1, 2, 3])
    



if __name__ == "__main__":
    unittest.main()