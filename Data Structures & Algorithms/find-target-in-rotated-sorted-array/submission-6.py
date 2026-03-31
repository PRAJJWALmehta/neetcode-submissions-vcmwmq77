class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            k = l + (r-l)//2

            if nums[k] > nums[r]:
                l = k+1
            else:
                r = k

        pivot = l
        l, r = 0, len(nums)-1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot-1
        
        while l <= r:
            k = l + (r-l)//2

            if nums[k] == target:
                return k
            elif nums[k] > target:
                r = k-1
            else:
                l = k+1
        
        return -1
