import unittest
from solution import NumArray

class TestSolution(unittest.TestCase):
    def setUp(self):
        nums = [-2, 0,  3, -5, 2, -1]
        self.numArray = NumArray(nums)
    
    def test_1(self):
        left = 0
        right = 2
        
        result = self.numArray.sumRange(left, right)
        self.assertEqual(result, 1)

    def test_2(self):
        left = 2
        right = 5
        
        result = self.numArray.sumRange(left, right)
        self.assertEqual(result, -1)

    def test_3(self):
        left = 0
        right = 5
        
        result = self.numArray.sumRange(left, right)
        self.assertEqual(result, -3)
        

if __name__ == "__main__":
    unittest.main()
