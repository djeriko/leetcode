import unittest
from solution import Solution, Interval

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        arr = [Interval(0,30), Interval(5,10), Interval(15,20)]
        result = self.solution.canAttendMeeting(arr)

        self.assertEqual(result, False)

    def test_2(self):
        arr = [Interval(5,8), Interval(9,15)]
        result = self.solution.canAttendMeeting(arr)

        self.assertEqual(result, True)

    def test_3(self):
        arr = [Interval(465,497),Interval(386,462),Interval(354,380),Interval(134,189),Interval(199,282),Interval(18,104),Interval(499,562),Interval(4,14),Interval(111,129),Interval(292,345)]
        result = self.solution.canAttendMeeting(arr)

        self.assertEqual(result, True)

    def test_4(self):
        arr = [Interval(0,8), Interval(8,10)]
        result = self.solution.canAttendMeeting(arr)

        self.assertEqual(result, True)
        

if __name__ == "__main__":
    unittest.main()
