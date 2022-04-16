from typing import List

class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        """
        Time - O(n)
        Space - O(n)
        """
        seen = set()
        for i in nums:
            if i in seen:
                seen.discard(i)
            else: 
                seen.add(i)
            
        return seen.pop()

    def singleNumber(self, nums: List[int]) -> int:
        """
        Time - O(n)
        Space - O(1)
        """
        mask = 0
        for i in nums:
            mask ^= i
        
        return mask
