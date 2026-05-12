class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = {}
        lis = 1

        def dfs(i, j):
            if (i, j) not in dp:
                res = 0
                for dr, dc in directions:
                    r = i+dr
                    c = j+dc
                    if r >= 0 and r < m and c >= 0 and c < n and matrix[i][j] < matrix[r][c]:
                        res = max(res, dfs(r, c))
                
                dp[(i, j)] = 1+res
            
            return dp[(i, j)]
        
        for i in range(m):
            for j in range(n):
               dfs(i, j)
        
        return max(dp.values())
