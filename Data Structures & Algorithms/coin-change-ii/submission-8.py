class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[amount] = 1

        for i in range(n-1, -1, -1):
            buff = [0]*(amount+1)
            buff[amount] = 1
            for amt in range(amount-1, -1, -1):
                buff[amt] += dp[amt]
                buff[amt] += buff[amt+coins[i]] if amt+coins[i] <= amount else 0
            dp = buff
        
        return dp[0]