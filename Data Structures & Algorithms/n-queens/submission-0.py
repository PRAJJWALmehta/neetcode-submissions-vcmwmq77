class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                temp = ["".join(i) for i in board]
                res.append(temp)
                return
            
            for c in range(n):
                if (c in cols) or (r+c in posDiag) or (r-c in negDiag):
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            
        backtrack(0)
        return res


            


        