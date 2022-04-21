import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        

    def test_1(self):
        data = ListNode(3)
        
        e1 = ListNode(2)
        e2 = ListNode(0)
        e3 = ListNode(-4)

        data.next = e1
        e1.next = e2
        e2.next = e3
        e3.next = e1

        result = self.solution.hasCycle(data)
        self.assertEqual(result, True)

    def test_2(self):
        data = ListNode(1)
        e1 = ListNode(2)
        data.next = e1
        e1.next = data

        result = self.solution.hasCycle(data)
        self.assertEqual(result, True)

    def test_2(self):
        data = ListNode(1)

        result = self.solution.hasCycle(data)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
