import unittest
from solution import NumArray

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.numArray = NumArray([1, 2])

    def test_1(self):
        left = 1
        right = 1
        
        result = self.numArray.sumRange(left, right)
        expected = [None, 1, -1, -3]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
