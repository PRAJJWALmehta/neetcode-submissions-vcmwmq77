class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0]*l2 for i in range(l1)]

        def dfs(i, j):
            if i >= l1 or j >= l2:
                return 0
            
            if not dp[i][j]:
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], 1+dfs(i+1, j+1))
                dp[i][j] = max(dp[i][j], dfs(i+1, j), dfs(i, j+1))
            
            return dp[i][j]
        
        return dfs(0, 0)
        