import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        head = ListNode().arrayToList([1,2,6,3,4,5,6])
        expected = ListNode().arrayToList([1,2,3,4,5])

        result = self.solution.removeElements(head, 6)
        self.assertEqual(result.toList(), expected.toList())

    def test_2(self):
        head = ListNode().arrayToList([7,7,7,7,7])

        result = self.solution.removeElements(head, 7)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
