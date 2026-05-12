class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[float('inf')]*(l2+1) for i in range(l1+1)]
        dp[l1][l2] = 0

        for i in range(l1+1):
            dp[i][l2] = l1-i
        
        for j in range(l2+1):
            dp[l1][j] = l2-j
        
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = dp[i][j+1]
                    delete = dp[i+1][j]
                    replace = dp[i+1][j+1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        
        return dp[0][0]

        # def dfs(i, j):
        #     if i == l1 and j == l2:
        #         return 0
        #     if i >= l1:
        #         return l2-j
        #     if j >= l2:
        #         return l1-i

        #     if (i, j) not in dp:
        #         if word1[i] == word2[j]:
        #             dp[(i, j)] = dfs(i+1, j+1)
        #         else:
        #             insert = dfs(i, j+1)
        #             delete = dfs(i+1, j)
        #             replace = dfs(i+1, j+1)

        #             dp[(i, j)] = 1 + min(insert, delete, replace)
            
        #     return dp[(i, j)]
        
        # return dfs(0, 0)
