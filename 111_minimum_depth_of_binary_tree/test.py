import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_1(self):
        result = self.solution.minDepth([3, 9, 20, None, 4, None, 5, None, 6])
        expected = 2
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
