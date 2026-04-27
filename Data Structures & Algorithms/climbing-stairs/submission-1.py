class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)

        def dfs(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            
            if not dp[num]:
                dp[num] = dfs(num-1) + dfs(num-2)
            
            return dp[num]
        
        dfs(n)
        return dp[n]

        