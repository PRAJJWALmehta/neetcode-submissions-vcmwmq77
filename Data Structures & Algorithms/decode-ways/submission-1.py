class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 and int(s) > 0 and int(s) < 10:
            return True
        if len(s) == 2 and int(s) > 9 and int(s) < 27:
            return True
        
        return False

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if i < n-1 and (s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7)):
                res += dfs(i+2)
            
            dp[i] = res
            return dp[i]
        
        return dfs(0)