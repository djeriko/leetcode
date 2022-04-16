import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        """
        Should return array [5, 6] from given input

        """
        input = [4, 3, 2, 7, 8, 2, 3, 1]
        result = self.solution.findDisappearedNumbers(input)
        expected = [5, 6]
        self.assertEqual(result, expected)

    def test_2(self):
        input = [1, 1]
        result = self.solution.findDisappearedNumbers(input)
        expected = [2]
        self.assertEqual(result, expected)
       

if __name__ == "__main__":
    unittest.main()
