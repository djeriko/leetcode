from typing import List

class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                seen.discard(i)
            else: 
                seen.add(i)
            
        return seen.pop()

    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for i in nums:
            mask ^= i
            print(mask)
        
        return mask
