class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = [[0]*(lt+1) for i in range(ls+1)]

        for i in range(ls, -1, -1):
            for j in range(lt, -1, -1):
                if j == lt:
                    dp[i][j] = 1
                    continue
                dp[i][j] += dp[i+1][j] if i+1 <= ls else 0
                if i < ls and j < lt and s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]


        