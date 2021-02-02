import unittest
from question7 import StringDict


class testq7(unittest.TestCase):
    def test_c1(self):
        dict = {"H": 1, "e": 1, "l": 2, "o": 1}
        self.assertEqual(StringDict("Hello"), dict)

    def test_c2(self):
        dict = {"H": 1, "i": 1}
        self.assertEqual(StringDict("Hi"), dict)



if __name__ == "__main__":
    unittest.main()