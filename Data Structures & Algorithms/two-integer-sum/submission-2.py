class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_map = {}

        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[val] = i 