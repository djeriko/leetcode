import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        data = [0, 1, 0]
        result = self.solution.peakIndexInMountainArray(data)
        self.assertEqual(result, 1)

    def test_2(self):
        data = [0, 2, 1, 0]
        result = self.solution.peakIndexInMountainArray(data)
        self.assertEqual(result, 1)

    def test_3(self):
        data = [0, 10, 5, 1, 0]
        result = self.solution.peakIndexInMountainArray(data)
        self.assertEqual(result, 1)

    def test_4(self):
        data = [1, 2, 3, 1]
        result = self.solution.peakIndexInMountainArray(data)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
