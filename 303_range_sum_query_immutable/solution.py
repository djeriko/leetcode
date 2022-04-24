from typing import List

class NumArray:
    """
    Time - O(1)
    Space - O(n)
    """
    def __init__(self, nums: List[int]):
        current_sum = 0
        self.sums = [0]
        for num in nums:
            current_sum += num 
            self.sums.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
