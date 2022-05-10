import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_1(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "a")
        self.assertEqual(result, "c")

if __name__ == "__main__":
    unittest.main()
        

