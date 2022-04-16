import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        result = self.solution.fib(2)
        self.assertEquals(result, 1)

    def test_2(self):
        result = self.solution.fib(4)
        self.assertEquals(result, 3)

if __name__ == "__main__":
    unittest.main()
