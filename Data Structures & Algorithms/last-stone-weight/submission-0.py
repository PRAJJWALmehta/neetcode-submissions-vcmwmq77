class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-val for val in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = abs(heapq.heappop(heap))
            y = abs(heapq.heappop(heap))

            if x-y:
                heapq.heappush(heap, y-x)
        
        return abs(heap[0]) if len(heap) else 0
