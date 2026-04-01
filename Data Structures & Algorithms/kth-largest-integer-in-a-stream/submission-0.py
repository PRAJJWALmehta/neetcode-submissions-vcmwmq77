class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [val for val in nums]
        self.maxSize = k        
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.maxSize:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
