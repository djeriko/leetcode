from typing import List

class Solution:
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
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
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        With set.
        """
        seen = set(x for x in range(1 ,len(nums) + 1))
        
        for i in nums:
            seen.discard(i)
        
        return list(seen)
        




