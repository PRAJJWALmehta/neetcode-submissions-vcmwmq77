class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set([])

        for i, val in enumerate(sorted_nums):
            j = i+1
            k = len(sorted_nums)-1

            while j < k:
                curr = sorted_nums[i] + sorted_nums[j]+sorted_nums[k]
                if curr == 0:
                    res.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
            
        return list(res)

                




        