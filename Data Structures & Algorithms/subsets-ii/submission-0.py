class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        buff = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(buff.copy())
                return
            
            buff.append(nums[i])
            backtrack(i+1)
            buff.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i+1
            backtrack(i+1)
        
        backtrack(0)
        return res