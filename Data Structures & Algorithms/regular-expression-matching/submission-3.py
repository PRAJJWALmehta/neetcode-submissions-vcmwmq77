class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False]*(lp+1) for i in range(ls+1)]
        dp[ls][lp] = True

        for i in range(ls, -1, -1):
            for j in range(lp-1, -1, -1):
                match = i < ls and ((s[i] == p[j]) or (p[j] == "."))
                if j+1 < lp and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2]
                    if match:
                        dp[i][j] = dp[i+1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = False
        
        return dp[0][0]
