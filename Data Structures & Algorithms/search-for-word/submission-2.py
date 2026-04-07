class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited:
                return False
            
            if board[r][c] == word[i]:
                visited.add((r, c))
                found = (
                    dfs(r-1, c, i+1) or
                    dfs(r+1, c, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r, c+1, i+1))
                visited.remove((r, c))
                return found
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
        