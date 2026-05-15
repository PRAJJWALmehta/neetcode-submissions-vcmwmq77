class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[-1] = 0

        for i in range(n-2, -1, -1):
            temp = float('inf')
            bound = min(i+nums[i]+1, n)
            for j in range(i+1, bound):
                temp = min(temp, 1+dp[j])
            dp[i] = temp
        
        return dp[0]
            