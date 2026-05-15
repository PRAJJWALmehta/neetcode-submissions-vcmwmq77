class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}

        def dfs(i):
            if i == n-1:
                return True
            if i >= n:
                return False

            if i not in dp:
                temp = False
                bound = min(nums[i], n - i)
                for j in range(bound, 0, -1):
                    temp = temp or dfs(i+j)
                    if temp:
                        break
                dp[i] = temp
            
            return dp[i]
        
        return dfs(0)