class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # add all the O's in the border to the queue
        # perform bfs to mark all the unbound O's

        ROWS, COLS = len(board),len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        unbound = set()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
                unbound.add((r, 0))
            
            if board[r][COLS-1] == "O":
                q.append((r, COLS-1))
                unbound.add((r, COLS-1))
        
        for c in range(COLS):
            if (0, c) not in unbound and board[0][c] == "O":
                q.append((0, c))
                unbound.add((0, c))
            
            if (ROWS-1, c) not in unbound and board[ROWS-1][c] == "O":
                q.append((ROWS-1, c))
                unbound.add((ROWS-1, c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and board[r][c] == "O" and (r, c) not in unbound:
                    q.append((r, c))
                    unbound.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in unbound:
                    board[r][c] = "X"





        