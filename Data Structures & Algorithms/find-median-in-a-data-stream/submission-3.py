class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if num > self.findMedian():
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.left) - len(self.right) > 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        if len(self.right) - len(self.left) > 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        

    def findMedian(self) -> float:
        if not self.right and not self.left:
            return 0

        diff = len(self.right) - len(self.left)

        if diff > 0:
            return self.right[0]
        elif diff < 0:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0])/2.0

        
        