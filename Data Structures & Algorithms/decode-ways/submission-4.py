class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = 0
        dp1 = 1
        dp2 = 0

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if i < n-1 and ( s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7)):
                dp += dp2
            
            dp2 = dp1
            dp1 = dp

            
        return dp1
        