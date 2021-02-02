import unittest
from question6 import rmwht


class testq6(unittest.TestCase):
    def test_c1(self):
        self.assertEqual(rmwht("Hi    my name    is xyz"), "Hi my name is xyz")

    def test_c2(self):
        self.assertEqual(rmwht("      Hi    my name    is xyz"), "Hi my name is xyz")

    def test_c3(self):
        self.assertEqual(rmwht("Hi    my name    is xyz        "), "Hi my name is xyz")


if __name__ == "__main__":
    unittest.main()

