class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_map = {}

        for i in range(len(nums)):
            if target - nums[i] in prev_map:
                return [prev_map[target-nums[i]], i]
            else:
                prev_map[nums[i]] = i