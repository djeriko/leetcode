import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome_1(self):
        s = "baab"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)

    def test_isPalindrome_2(self):
        s = "mama"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, False)

    def test_isPalindrome_3(self):
        s = "bb"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)

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

    def test_3(self):
        s = "eabcb"
        expect = "bcb"
        result = self.solution.longestPalindrome(s) 
        self.assertEqual(result, expect)

    def test_4(self):
        s = "baab"
        expect = "baab"
        result = self.solution.longestPalindrome(s) 
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()
