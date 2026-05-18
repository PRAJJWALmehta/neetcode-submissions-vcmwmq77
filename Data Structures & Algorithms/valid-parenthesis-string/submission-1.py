class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = {}

        def dfs(i, left):
            if i == n:
                if left == 0:
                    return True
                else:
                    return False
            
            if (i, left) not in dp:
                if s[i] == "(":
                    dp[(i, left)] = dfs(i+1, left+1)
                elif s[i] == ")":
                    dp[(i, left)] = dfs(i+1, left-1) if left else False
                else:
                    dp[(i, left)] = dfs(i+1, left+1) or dfs(i+1, left-1) or dfs(i+1, left)
            
            return dp[(i, left)]
        
        return dfs(0, 0)