class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0]*(N+1)

        def dfs(num):
            if num >= N:
                return 0
            
            if not dp[num]:
                dp[num] = cost[num] + min(dfs(num+1), dfs(num+2))
            
            return dp[num]
        
        return min(dfs(0), dfs(1))