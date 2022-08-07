import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        data = [1, 2, 3, 4]
        m = 2
        n = 2
        expected = [[1, 2], [3, 4]]
        result = self.solution.construct2DArray(data, m, n)
        self.assertEqual(result, expected)

    def test_2(self):
        data = [1, 2, 3]
        m = 1
        n = 3
        expected = [[1, 2, 3]]
        result = self.solution.construct2DArray(data, m, n)
        self.assertEqual(result, expected)

    def test_3(self):
        data = [1, 2]
        m = 1
        n = 1
        expected = []
        result = self.solution.construct2DArray(data, m, n)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
