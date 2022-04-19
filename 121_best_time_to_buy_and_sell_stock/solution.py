from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = prices[0]
        profit = 0
        for price in prices:
            if price < currentMin:
                currentMin = price
                
            if profit < price - currentMin:
                profit = price - currentMin
            
        return profit
                
                
                

