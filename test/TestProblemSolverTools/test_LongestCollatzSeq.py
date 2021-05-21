import sys
sys.path.insert(1, "../../")
import src.ProblemSolverTools.LongestCollatzSeq as tools
import unittest

class TestMultiplesOf3and5(unittest.TestCase):
    def setUp(self):
        self.even1 = 150
        self.even2 = 41 
        self.next_term_1 = 5 
        self.next_term_2 = 10
        self.collatz_seq_len = 4
        self.max_collatz_len = 4
        
    def test_even(self):
        self.assertTrue(tools.even(self.even1))
        self.assertFalse(tools.even(self.even2))
        
    def test_next_term(self):
        self.assertEqual(tools.next_term(self.next_term_1), 16)
        self.assertEqual(tools.next_term(self.next_term_2), 5)
        
    def test_collatz_seq_len(self):
        self.assertEqual(tools.collatz_seq_len(self.collatz_seq_len), 3)
    
    def test_max_collatz_len(self):
        self.assertEqual(tools.longest_collatz_end(self.max_collatz_len), 3)
    
        
if __name__ == '__main__':
    unittest.main()
    