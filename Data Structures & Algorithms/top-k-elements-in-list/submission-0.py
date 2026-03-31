class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        min_heap = []
        for i in freq.keys():
            heapq.heappush(min_heap, (freq[i], i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        for i in range(k):
            res.append(min_heap[0][1])
            heapq.heappop(min_heap)

        return res
