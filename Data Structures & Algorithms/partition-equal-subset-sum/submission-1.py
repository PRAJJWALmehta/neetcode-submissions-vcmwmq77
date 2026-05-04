class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        for val in nums:
            target += val

        if target/2 != target//2:
            return False

        target /= 2

        n = len(nums)
        dp = [False]*n

        def dfs(i, curr):
            print(i, curr)
            if curr == 0:
                return True
            
            if i >= n or curr < 0:
                return False
            
            if not dp[i]:
                dp[i] = dfs(i+1, curr-nums[i]) or dfs(i+1, curr)
            
            return dp[i]
        
        dfs(0, target)
        return dp[0]


        