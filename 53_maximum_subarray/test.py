import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = self.solution.maxSubArray(data)
        self.assertEqual(result, 6)

    def test_2(self):
        data = [1]
        result = self.solution.maxSubArray(data)
        self.assertEqual(result, 1)

    def test_3(self):
        data = [5, 4, -1, 7, 8]
        result = self.solution.maxSubArray(data)
        self.assertEqual(result, 23)

    def test_4(self):
        data = [-2, -1]
        result = self.solution.maxSubArray(data)
        self.assertEqual(result, -1)

    def test_5(self):
        data = [-1, 0]
        result = self.solution.maxSubArray(data)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()

