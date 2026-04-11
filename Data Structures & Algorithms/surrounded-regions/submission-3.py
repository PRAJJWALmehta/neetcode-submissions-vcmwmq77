class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # add all the O's in the border to the queue
        # perform bfs to mark all the unbound O's

        ROWS, COLS = len(board),len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(ROWS):
            for c in [0, COLS-1]:
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "U"
        
        for c in range(COLS):
            for r in [0, ROWS-1]:
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "U"
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "U"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "U":
                    board[r][c] = "O"





        