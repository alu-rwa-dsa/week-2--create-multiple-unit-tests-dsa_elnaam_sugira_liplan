import unittest
from question2 import StringDict


class testq2(unittest.TestCase):
    def test_c1(self):
        dict = {"H": 1, "e": 1, "l": 2, "o": 1}
        self.assertEqual(StringDict("Hello"), dict)

    def test_c2(self):
        dict = {"H": 1, "i": 1}
        self.assertEqual(StringDict("Hi"), dict)

    def test_c3(self):
        dict = {"H": 1}
        self.assertEqual(StringDict("H"), dict)



if __name__ == "__main__":
    unittest.main()
