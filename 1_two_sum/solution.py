class Solution:
    '''
    Time - O(n)
    Space - O(n)
    Pattern - HashTable
    '''
    def twoSum(self, nums: [], target: int):
        seen = {}
        for i in range(len(nums)): 
            if target - nums[i] in seen:
                return [seen[target - nums[i]] ,i]
            seen[nums[i]] = i
        
        return []

