class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [0]*(l2+1)

        for i in range(l1-1, -1, -1):
            buff = [0]*(l2+1)
            for j in range(l2-1, -1, -1):
                if text1[i] == text2[j]:
                    buff[j] = 1+dp[j+1]
                buff[j] = max(buff[j], dp[j], buff[j+1])
            dp = buff
        
        return dp[0]
        