class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        n = len(coins)
        dp = [-1]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            temp = float('inf')
            for c in coins:
                if i-c >= 0:
                    temp = min(temp, 1+dp[i-c])
            dp[i] = temp
        
        return dp[amount] if dp[amount] != float('inf') else -1