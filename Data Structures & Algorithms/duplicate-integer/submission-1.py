class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort();

        for curr in range(len(nums)-1):
            next = curr+1
            if nums[curr] == nums[next]:
                return True

        
        return False


        