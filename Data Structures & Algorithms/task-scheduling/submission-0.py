class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        heap = []
        q = deque()
        time = 0
        res = []

        for task in tasks:
            count[task] += 1
        
        for task in count:
            heapq.heappush(heap, -count[task])
        
        while heap or q:
            time += 1
            if q and q[0][0] < time:
                heapq.heappush(heap, q[0][1])
                q.popleft()

            if heap:
                freq = heapq.heappop(heap)
                freq += 1
                if freq:
                    q.append([time+n, freq])
        
        return time

            

        