class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0

        for val in nums:
            temp = max(rob2, rob1+val)
            rob1 = rob2
            rob2 = temp
        
        return rob2
