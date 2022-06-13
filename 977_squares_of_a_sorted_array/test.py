import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_1(self):
        data = [-4, -1, 0, 3, 10]
        result = self.solution.sortedSquares(data)
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(result, expected)

    def test_2(self):
        data = [-7, -3, 2, 3, 11]
        result = self.solution.sortedSquares(data)
        expected = [4, 9, 9, 49, 121]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

