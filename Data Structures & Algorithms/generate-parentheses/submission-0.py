class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        string = []
        
        def backtrack(l, r):
            if len(string) == 2*n:
                res.append("".join(string.copy()))
                return
        
            # add a left bracket and reduce l count
            if l:
                string.append("(")
                stack.append("(")
                backtrack(l-1, r)
                string.pop()
                stack.pop()

            # add a right bracket if         
            if stack and stack[-1] == "(":
                string.append(")")
                stack.pop()
                backtrack(l, r-1)
                stack.append("(")
                string.pop()
            
        
        backtrack(n, n)
        return res


