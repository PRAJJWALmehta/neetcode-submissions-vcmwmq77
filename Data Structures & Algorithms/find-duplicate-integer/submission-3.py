class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0]*len(nums)

        for val in nums:
            if seen[val]:
                return val
            seen[val] += 1
        