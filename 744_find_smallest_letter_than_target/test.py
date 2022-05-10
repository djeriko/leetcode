import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_1(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "a")
        self.assertEqual(result, "c")

    def test_2(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "c")
        self.assertEqual(result, "f")

    def test_3(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "d")
        self.assertEqual(result, "f")

    def test_4(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "j")
        self.assertEqual(result, "c")

    def test_5(self):
        data = ["c", "f", "j"]
        result = self.solution.nextGreatestLetter(data, "f")
        self.assertEqual(result, "j")

if __name__ == "__main__":
    unittest.main()
        
