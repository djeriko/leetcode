import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        data = [7, 1, 5, 3, 6, 4]
        result = self.solution.maxProfit(data)
        self.assertEqual(result, 5)

    def test_2(self):
        data = [7, 6, 4, 3, 1]
        result = self.solution.maxProfit(data)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()

