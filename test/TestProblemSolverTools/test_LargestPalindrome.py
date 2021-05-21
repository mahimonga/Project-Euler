import sys

sys.path.insert(1, "../../")
import Problem4_11.largest_palindrome as tools
import unittest


class TestLargestPalindrom(unittest.TestCase):
    def setUp(self):
        self.upperLimit1 = 2
        self.upperLimit2 = 3
        self.lowerLimit1 = 2
        self.lowerLimit2 = 4
        self.reversedNumber1 = 4098

        self.reversedNumber2 = 3789
        self.palindrome1 = 9009
        self.palindrome2 = 1001

    def test_upper_limit(self):
        self.assertTrue(tools.upper_limit(self.upperLimit1), 99)
        self.assertFalse(tools.upper_limit(self.upperLimit2), 99)

    def test_lower_limit(self):
        self.assertTrue(tools.lower_limit(self.lowerLimit1), 10)
        self.assertFalse(tools.lower_limit(self.lowerLimit1), 100)

    def test_reversed_number(self):
        self.assertTrue(tools.reverse(self.reversedNumber1), 8904)
        self.assertFalse(tools.reverse(self.reversedNumber2), 987)

    def test_isPalindrome_number(self):
        self.assertTrue(tools.isPalindrome(self.palindrome1), True)
        self.assertFalse(tools.isPalindrome(self.palindrome2), False)


if __name__ == '__main__':
    unittest.main()
