class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        visited = set()
        heap = [(0, 0)]
        res = 0

        # for i in range(N):
        #     x1, y1 = points[i]
        #     for j in range(i+1, N):
        #         x2, y2 = points[j]
        #         dist = abs(x1-x2) + abs(y1-y2)
        #         adj[i].append((dist, j))
        #         adj[j].append((dist, i))
        
        while len(visited) < N:
            dist, p = heapq.heappop(heap)
            if p in visited:
                continue
            res += dist
            visited.add(p)

            for n in range(N):
                if n not in visited:
                    x1, y1 = points[p]
                    x2, y2 = points[n]
                    ndist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heap, (ndist, n))
                    
        
        return res
        
