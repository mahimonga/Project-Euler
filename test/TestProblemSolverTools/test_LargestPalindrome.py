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
        self.assertTrue(tools.upper_limit(self.upperLimit2), 999)

    def test_lower_limit(self):
        self.assertTrue(tools.lower_limit(self.lowerLimit1), 10)
        self.assertTrue(tools.lower_limit(self.lowerLimit1), 1000)

    def test_reversed_number(self):
        self.assertTrue(tools.reverse(self.reversedNumber1), 8904)
        self.assertTrue(tools.reverse(self.reversedNumber2), 9873)

    def test_isPalindrome_number(self):
        self.assertTrue(tools.isPalindrome(self.palindrome1), True)
        self.assertTrue(tools.isPalindrome(self.palindrome2), True)


if __name__ == '__main__':
    unittest.main()
