class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        n = len(coins)
        dp = [-1]*(amount+1)

        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            
            if dp[amt] == -1:
                temp = float('inf')
                for c in coins:
                    temp = min(temp, 1+dfs(amt-c))
                dp[amt] = temp
            
            return dp[amt]
        
        dfs(amount)
        return dfs(amount) if dp[amount] != float('inf') else -1