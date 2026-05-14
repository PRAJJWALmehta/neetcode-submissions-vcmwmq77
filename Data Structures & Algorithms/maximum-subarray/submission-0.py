class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dq = deque()
        res = -float('inf')
        temp = 0

        for val in nums:
            dq.append(val)
            temp += val
            res = max(res, temp)
            if temp < 0:
                dq.clear()
                temp = 0
        
        return res
