import unittest
from question8 import linkedListMerge


class testq8(unittest.TestCase):
    def test_c1(self):
        self.assertFalse(len(linkedListMerge([["a", "b", "b"], "c", "d"])) > len(["a", "b", "c", "d"]))

    def test_c2(self):
        self.assertIn("b", linkedListMerge([["a", "b", "b"], "c", "d"]))

    def test_c3(self):
        self.assertIsNotNone(linkedListMerge([["a", "b", "b"], "c", "d"]))



if __name__ == "__main__":
    unittest.main()