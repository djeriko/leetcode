import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        """
        Should return 1 from array [2, 2, 1]
        """
        input = [2, 2, 1]
        result = self.solution.singleNumber(input)
        self.assertEqual(result, 1)

    def test_2(self):
        """
        Should return 1 from array [4, 1, 2, 1, 2]
        """
        input = [4, 1, 2, 1, 2]
        result = self.solution.singleNumber(input)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
        
    
