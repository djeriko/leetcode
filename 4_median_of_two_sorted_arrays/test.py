import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        nums1 = [1, 3]
        nums2 = [2, 4]
        self.assertEqual(self.solution.mergeSortedArrays(nums1, nums2), [1, 2, 3, 4])

    def test_merge_2(self):
        nums1 = [2]
        nums2 = [1, 3]
        self.assertEqual(self.solution.mergeSortedArrays(nums1, nums2), [1, 2, 3])
    
    def test_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.0) 

    def test_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5) 

if __name__ == "__main__":
    unittest.main()

    
    
