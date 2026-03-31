class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0

        for i in nums:
            if i-1 not in arr:
                length = 1
                while i+1 in arr:
                    length += 1
                    i += 1
                res = max(res, length)
        
        return res
