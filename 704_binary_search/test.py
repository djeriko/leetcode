import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_1(self):
        data = [-1, 0, 3, 5, 9, 12]
        target = 9
        result = self.solution.binarySearch(data, target)
        self.assertEqual(result, 4)

    def test_2(self):
        data = [-1, 0, 3, 5, 9, 12]
        target = 2
        result = self.solution.binarySearch(data, target)
        self.assertEqual(result, -1)

    def test_3(self):
        data = [12]
        target = 12
        result = self.solution.binarySearch(data, target)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
