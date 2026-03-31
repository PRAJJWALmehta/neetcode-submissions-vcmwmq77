class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        zeros = 0

        for i in nums:
            if i:
                p *= i
            else:
                zeros += 1
        
        if zeros > 1: return [0]*len(nums)
        
        for i in nums:
            if zeros:
                if i == 0:
                    res.append(p)
                else:
                    res.append(0)
            else:
                res.append(p//i)
        
        return res