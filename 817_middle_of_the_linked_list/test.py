import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        tail = head = ListNode(1)
        for x in [2, 3, 4, 5, 6]:
            tail.next = ListNode(x)
            tail = tail.next
        
        result = self.solution.middleNode(head)
        resultList = []
        while result:
            resultList.append(result.val)
            result = result.next
        self.assertEqual([4, 5, 6], resultList)

if __name__ == "__main__":
    unittest.main()
