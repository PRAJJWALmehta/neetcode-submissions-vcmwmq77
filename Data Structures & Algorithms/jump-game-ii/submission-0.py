class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def dfs(i):
            if i == n-1:
                return 0
            
            if i not in dp:
                temp = float('inf')
                bound = min(i+nums[i]+1, n)
                for j in range(i+1, bound):
                    temp = min(temp, 1+dfs(j))
                dp[i] = temp
            
            return dp[i]
        
        return dfs(0)

            