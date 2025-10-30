class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v, max_profit, cur = prices[0],0,0
        for i in range(1,len(prices)):
            cur = prices[i] - min_v
            if cur > max_profit: 
                max_profit = cur
            if prices[i] < min_v: 
                min_v = prices[i]
        return max_profit