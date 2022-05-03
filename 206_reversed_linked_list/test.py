import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def listNodeToList(self, head: ListNode):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_1(self):
        input = None
        for x in [1,2,3,4,5]:
            input = ListNode(x, input)
        
        expected = None
        for x in [5,4,3,2,1]:
            expected = ListNode(x, expected)

        result = self.solution.reversedList(input)

        self.assertEqual(self.listNodeToList(result), self.listNodeToList(expected))
            
if __name__ == "__main__":
    unittest.main()
