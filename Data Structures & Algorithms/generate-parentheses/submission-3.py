class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(l, r):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            
            if l:
                stack.append("(")
                backtrack(l-1, r)
                stack.pop()
            
            if r-l:
                stack.append(")")
                backtrack(l, r-1)
                stack.pop()
        
        backtrack(n, n)
        return res


