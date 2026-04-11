class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        q_pac = deque()
        q_atl = deque()
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            q_pac.append((r, 0))
            pacific.add((r, 0))

            q_atl.append((r, COLS-1))
            atlantic.add((r, COLS-1))
        
        for c in range(COLS):
            if (0, c) not in pacific:
                q_pac.append((0, c))
                pacific.add((0, c))

            if (ROWS-1, c) not in atlantic:
                q_atl.append((ROWS-1, c))
                atlantic.add((ROWS-1, c))
        
        while q_pac:
            row, col = q_pac.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in pacific and heights[r][c] >= heights[row][col]:
                    pacific.add((r, c))
                    q_pac.append((r, c))
        
        
        while q_atl:
            row, col = q_atl.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in atlantic and heights[r][c] >= heights[row][col]:
                    atlantic.add((r, c))
                    q_atl.append((r, c))
        
        return [list(cell) for cell in (atlantic & pacific)]



