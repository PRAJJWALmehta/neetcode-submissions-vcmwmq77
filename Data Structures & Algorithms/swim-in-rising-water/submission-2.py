class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        heap = [(grid[0][0], 0, 0)]
        
        visited.add((0, 0))

        while heap:
            time, row, col = heapq.heappop(heap)
            if row == ROWS-1 and col == COLS-1:
                return time
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited:
                    continue
                visited.add((r, c))
                heapq.heappush(heap, (max(time, grid[r][c]),r, c))
        