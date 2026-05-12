class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(int)

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            
            if (i, j) not in dp:
                dp[(i, j)] = dfs(i+1, j)
                if s[i] == t[j]:
                    dp[(i, j)] += dfs(i+1, j+1)
            
            return dp[(i, j)]
        
        return dfs(0, 0)


        