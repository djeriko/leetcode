from typing import List

class Solution:
    def findDisappearedNumbers_0(self, nums: List[int]) -> List[int]:
        '''
        Simple solution.
        Time = O(n^2)
        Space = O(n)
        '''
        res = []
        for i in range(len(nums) + 1):
            if i == 0:
                continue
            if i not in nums:
                res.append(i)
                
        return res
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        """
        With set.
        Time = O(n)
        Space = O(n)
        """
        seen = set(x for x in range(1 ,len(nums) + 1))
        
        for i in nums:
            seen.discard(i)
        
        return list(seen)
        
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        From leetcode.
        Time = O(n)
        Space = O(1) if not count result array
        """
        
        # Mark existing value with negative number
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        
        return res 
