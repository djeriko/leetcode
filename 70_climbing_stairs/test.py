import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        result = self.solution.climbStairs(2)
        self.assertEqual(result, 2)

    def test_2(self):
        result = self.solution.climbStairs(3)
        self.assertEqual(result, 3)

    def test_3(self):
        result = self.solution.climbStairs(5)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
        
    
        
