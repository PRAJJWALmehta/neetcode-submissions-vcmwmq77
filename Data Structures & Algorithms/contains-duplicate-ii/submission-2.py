class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        dup = set()
        dq = deque()

        for val in nums:
            if len(dq) > k:
                dup.remove(dq[0])
                dq.popleft()
            
            if val in dup:
                return True
            
            dq.append(val)
            dup.add(val)
        
        return False