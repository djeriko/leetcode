import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        l1 = ListNode().fromList([1,2,4])
        l2 = ListNode().fromList([1,3,4])
        expected = ListNode().fromList([1,1,2,3,4,4])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(result.toList(), expected.toList())

if __name__ == "__main__":
    unittest.main()
