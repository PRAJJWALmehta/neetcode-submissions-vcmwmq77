class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, [-dist, point])
            if len(heap) > k:
                heapq.heappop(heap)
        
        for pair in heap:
            res.append(pair[1])
        
        return res
        