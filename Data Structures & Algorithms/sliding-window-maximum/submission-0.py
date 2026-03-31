class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        dq = deque()
        res = []

        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if r >= k-1:
                res.append(nums[dq[0]])
                if dq[0] == l:
                    dq.popleft()
                l += 1
        
        return res

        