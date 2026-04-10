class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        land_cell = 2**31-1
        q = deque()
        dist = 1

        # place all the treasure cells in the queue
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append((r, c))
        

        # start computing the distance in all directions of the treasure cells
        while q:
            print(q)
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == land_cell:
                        grid[r][c] = dist
                        q.append((r, c))
            
            dist += 1
