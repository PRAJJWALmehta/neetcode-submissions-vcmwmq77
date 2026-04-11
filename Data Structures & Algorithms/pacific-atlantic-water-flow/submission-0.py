class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        q = deque()
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # add all the coastal elements to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in pacific and heights[r][c] >= heights[row][col]:
                    pacific.add((r, c))
                    q.append((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS-1 or c == COLS-1:
                    atlantic.add((r, c))
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in atlantic and heights[r][c] >= heights[row][col]:
                    atlantic.add((r, c))
                    q.append((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        
        return res




