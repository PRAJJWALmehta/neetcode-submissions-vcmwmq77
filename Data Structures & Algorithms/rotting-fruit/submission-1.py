class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh:
            print(q)
            rotten = len(q)
            print(rotten)
            for i in range(rotten):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                        continue
                    q.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1
            time += 1
        
        print(fresh)
        return time if not fresh else -1
                


