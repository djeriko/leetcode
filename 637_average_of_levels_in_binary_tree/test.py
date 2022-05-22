import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        root = TreeNode.fromList([3,9,20,None,None,15,7])
        
        result = self.solution.averageOfLevels(root)
        expected = [3.0000, 14.5, 11.0]
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
