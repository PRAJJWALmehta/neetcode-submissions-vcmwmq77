class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for isBuying in [True, False]:
                if isBuying:
                    buy = dp[i+1][False] - prices[i] if i+1 < n else -prices[i]
                    cooldown = dp[i+1][isBuying] if i+1 < n else 0
                    dp[i][isBuying] = max(buy, cooldown)
                else:
                    sell = dp[i+2][True] + prices[i] if i+2 < n else  prices[i]
                    cooldown = dp[i+1][isBuying] if i+1 < n else 0
                    dp[i][isBuying] = max(sell, cooldown)
        
        return dp[0][True]
