import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        result = self.solution.twoSum([2,7,11,15], 9)
        self.assertEqual(result, [0,1])

    def test_2(self):
        result = self.solution.twoSum([3,2,4], 6)
        self.assertEqual(result, [1,2])

    def test_3(self):
        result = self.solution.twoSum([3,3], 6)
        self.assertEqual(result, [0,1])
        
if __name__ == "__main__":
    unittest.main()
