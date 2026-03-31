class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        base = 100000

        for val in nums:
            if nums[val%base-1] >= base:
                return val%base
            
            nums[val%base-1] = nums[val%base-1] + base

        