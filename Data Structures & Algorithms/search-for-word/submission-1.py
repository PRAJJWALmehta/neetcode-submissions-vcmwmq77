class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(r, c, i) -> bool:
            if i == len(word):
                return True       
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            
            if board[r][c] == word[i]:
                visited.add((r, c))
                if (r-1, c) not in visited:
                    if dfs(r-1, c, i+1): return True
                if (r, c+1) not in visited:
                    if dfs(r, c+1, i+1): return True
                if (r+1, c) not in visited:
                    if dfs(r+1, c, i+1): return True
                if (r, c-1) not in visited:
                    if dfs(r, c-1, i+1): return True
                visited.remove((r, c))
            
            return False
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False

                