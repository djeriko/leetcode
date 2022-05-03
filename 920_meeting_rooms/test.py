import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        arr = [(0,30), (5,10), (15,20)]
        result = self.solution.canAttendMeeting(arr)
        
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
