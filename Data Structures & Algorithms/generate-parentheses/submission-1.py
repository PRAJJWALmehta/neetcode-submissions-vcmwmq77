class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        string = []
        
        def backtrack(l, r):
            if len(string) == 2*n:
                res.append("".join(string.copy()))
                return
        
            if l:
                string.append("(")
                stack.append("(")
                backtrack(l-1, r)
                string.pop()
                stack.pop()

            if r-l:
                string.append(")")
                stack.pop()
                backtrack(l, r-1)
                stack.append("(")
                string.pop()
            
        
        backtrack(n, n)
        return res


