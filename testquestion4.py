import unittest
from question9 import TwoLists

class testq9(unittest.TestCase):
    def test_c1(self):
        a = [2, 7, 9, 4, 11, 3]
        b = [7, 9, 4, 11, 3]
        self.assertEqual(TwoLists(a, b), 2)
    
    def test_c2(self):
        a = [2, 7, 9, 4, 11, 3]
        b = [7, 9, 4, 11, 3]
        self.assertNotEqual(TwoLists(a, b), 8)
    
    def test_c3(self):
        a = [2, 7, 9, 4, 11, 3]
        b = [7, 9, 4, 11, 3]
        self.assertIsNotNone(TwoLists(a, b))




if __name__ == "__main__":
    unittest.main()
