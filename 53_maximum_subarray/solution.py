from typing import List

class Solution:
    def maxSubArray_0(self, nums: List[int]) -> int:
        """
        Brute Force.
        Time = O(n^2)
        Space = O(1)
        """
        curr_max = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sum = sum(nums[i:j+1])
                if curr_sum > curr_max:
                    curr_max = curr_sum

        return curr_max

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm.
        Time = O(n)
        Space = O(1)
        """
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
            
