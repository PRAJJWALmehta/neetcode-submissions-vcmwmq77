class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_p = prices[0]

        for sell_p in prices:
            max_p = max(max_p, sell_p - min_p)
            min_p = min(min_p, sell_p)
        
        return max_p