class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        def dfs(i):
            if i >= n:
                return 0
            
            if not dp[i]:
                dp[i] = max(dfs(i+2)+nums[i], dfs(i+1))
            
            return dp[i]
        
        return dfs(0)