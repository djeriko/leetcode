import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        head = None
        for x in [1, 2, 2, 1]:
            head = ListNode(x, next=head)

        result = self.solution.isPalindrome(head)
        self.assertEqual(result, True)

    def test_2(self):
        head = ListNode(1)
        node_0 = ListNode(2)
        head.next = node_0
        
        result = self.solution.isPalindrome(head)
        self.assertEqual(result, False)

    def test_3(self):
        head = ListNode(1)
        
        result = self.solution.isPalindrome(head)
        self.assertEqual(result, True)

    def test_4(self):
        head = None
        for x in [1, 0, 1]:
            head = ListNode(x, next=head)

        result = self.solution.isPalindrome(head)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
