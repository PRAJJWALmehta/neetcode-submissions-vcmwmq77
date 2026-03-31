class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            key = (r+l)//2

            if nums[key] == target:
                return key
            elif nums[key] > target:
                r = key-1
            else:
                l = key+1
        
        return -1

            