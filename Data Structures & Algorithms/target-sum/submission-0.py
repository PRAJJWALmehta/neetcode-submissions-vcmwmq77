class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, currSum):
            if i >= len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            
            if (i, currSum) not in dp:
                dp[(i, currSum)] = dfs(i+1, currSum+nums[i]) + dfs(i+1, currSum-nums[i])
            
            return dp[(i, currSum)]
        
        return dfs(0, 0)