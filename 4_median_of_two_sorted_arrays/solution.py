from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeSortedArrays(nums1, nums2)
        nums_len = len(nums)
        isEven = nums_len % 2 == 0        
        
        if isEven:
            middle_down = int(nums_len / 2 - 1)
            middle_up = middle_down + 1
            return (nums[middle_down] + nums[middle_up]) / 2
         
        else: 
            middle = int((nums_len / 2) + 0.5) - 1
            return nums[middle]

    def mergeSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        result_len = len(nums1) + len(nums2)
        
        for i in range(result_len):
            if len(nums1) == 0:
                result = result + nums2
                return result
            if len(nums2) == 0:
                result = result + nums1
                return result

            if nums1[0] > nums2[0]:
                result.append(nums2[0])
                nums2.pop(0)
            elif nums1[0] < nums2[0]: 
                result.append(nums1[0])
                nums1.pop(0)
            else:
                result.append(nums1[0])
                result.append(nums2[0])
                nums1.pop(0)
                nums2.pop(0)

        return result
        
                    
            
        
            
