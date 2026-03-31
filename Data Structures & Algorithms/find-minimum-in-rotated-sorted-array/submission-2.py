class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]

        while l <= r:
            k = l + (r-l)//2
            res = min(res, nums[k])


            if nums[k] <= nums[r]:
                res = min(res, nums[r])
                r = k-1

            if nums[k] >= nums[l]:
                res = min(res, nums[l])
                l = k+1
        
        return res

