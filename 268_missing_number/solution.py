from typing import List

class Solution: 
    def missingNumber_0(self, nums: List[int]) -> int:
        """
        Simple solution
        Time: O(n^2)
        Space: O(1)
    
        """
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
    def missingNumber_1(self, nums: List[int]) -> int:
        """
        Arifmetical solution.
        Time - O(n)
        Space - O(1)
        """
        return (1 + len(nums))/2 * len(nums) - sum(nums)

    def missingNumber(self, nums: List[int]) -> int:
        
        """
        Binary XOR solutiion.
        Time - O(n)
        Space - O(1)
        """
        res = len(nums)
        
        for i in range(len(nums)):
            res ^= i^nums[i]

        return res
