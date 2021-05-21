import sys
sys.path.insert(1, "../../")
import src.ProblemSolverTools.MultiplesOf3and5 as tools
import unittest

class TestMultiplesOf3and5(unittest.TestCase):
    def setUp(self):
        self.multiple1 = 150
        self.multiple2 = 46 
        self.multiple_list_1 = 5 
        self.multiple_list_2 = 10
        self.multiple_sum_1 = 10
        self.multiple_sum_2 = 4
        
    def test_is_multiple(self):
        self.assertTrue(tools.is_multiple(self.multiple1))
        self.assertFalse(tools.is_multiple(self.multiple2))
        
    def test_multiples(self):
        self.assertEqual(tools.multiples(self.multiple_list_1), [0, 3])
        self.assertEqual(tools.multiples(self.multiple_list_2), [0, 3, 5, 6, 9])
        
    def test_sum_of_multiples(self):
        self.assertEqual(tools.sum_of_multiples(self.multiple_sum_1), 23)
        self.assertEqual(tools.sum_of_multiples(self.multiple_sum_2), 3)
        
if __name__ == '__main__':
    unittest.main()
    