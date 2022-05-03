import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_1(self):
        head = ListNode().fromList([1,1,2])
        expected = ListNode().fromList([1,2])
        result = self.solution.deleteDuplicates(head) 
        self.assertEqual(result.toList(), expected.toList())

    def test_2(self):
        result = self.solution.deleteDuplicates(None) 
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
