class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        arr = sorted(nums)
        res = 1
        curr_max = 1


        for i in range(1, len(nums)):
            if arr[i] == arr[i-1]:
                continue
            elif arr[i] == arr[i-1] + 1:
                curr_max += 1
            else:
                curr_max = 1
            res = max(res, curr_max)
        
        return res
                




        