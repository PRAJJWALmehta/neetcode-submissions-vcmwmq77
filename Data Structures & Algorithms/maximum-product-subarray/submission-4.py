class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for i in nums:
            temp = i*curMax
            curMax = max(i, i*curMax, i*curMin)
            curMin = min(i, temp, i*curMin)
            res = max(res, curMax)
        
        return res