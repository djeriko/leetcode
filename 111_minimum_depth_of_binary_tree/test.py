import unittest
from solution import Solution, TreeNode

# TODO: Fix second test passing. 
# Solution actualu pass in Leetcode, but toBinaryTree function works incorrenct.

def toBinaryTree(items: [int]) -> TreeNode:
    n = len(items)
    if n == 0:
        return None
    
    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None
        
        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()
     

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_1(self):
        data = [3, 9, 20, None, None, 15, 7]
        root = toBinaryTree(data)
        result = self.solution.minDepth(root)
        expected = 2
        self.assertEqual(result, expected)
        
    def test_2(self):
        data = [2, None, 3, None, 4, None, 5, None, 6]
        root = toBinaryTree(data)
        result = self.solution.minDepth(root)
        expected = 5
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
