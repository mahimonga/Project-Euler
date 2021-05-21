import sys
sys.path.insert(1, "../../")
import src.ProblemSolver as ps
import unittest
SOLUTION = {1: 233168, 2: 4613732, 3: 6857, 4: 906609, 5: 232792560, 6: 25164150,
7: 104743, 8: 23514624000, 9: 31875000, 10: 142913828922, 11: 70600674, 12: 76576500,
13: 5537376230, 14: 837799}

class TestProblems(unittest.TestCase):
    def setUp(self):
        self.solver = ps.ProblemSolver()
        
    def test_problem1(self):
        self.assertEqual(self.solver.solve_problem1(), SOLUTION[1])
    
    def test_problem14(self):
        self.assertEqual(self.solver.solve_problem14(), SOLUTION[14])
     