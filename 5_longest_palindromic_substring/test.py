import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome_1(self):
        s = "baab"
        resutl = self.solution.isPalindrome(s)
        self.assertEqual(resutl, True)

    def test_isPalindrome_2(self):
        s = "mama"
        resutl = self.solution.isPalindrome(s)
        self.assertEqual(resutl, False)

    def test_1(self):
        s = "babad"
        expect = "bab"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expect)

    def test_2(self):
        s = "cbbd"
        expect = "bb"
        result = self.solution.longestPalindrome(s) 
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()
