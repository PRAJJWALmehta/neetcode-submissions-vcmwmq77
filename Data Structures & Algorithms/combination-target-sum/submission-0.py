class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        buff = []

        def dfs(idx: int, sum: int):
            if not sum:
                res.append(buff.copy())
                return
            if idx >= len(nums) or sum < 0:
                return
            
            buff.append(nums[idx])
            dfs(idx, sum-nums[idx])
            
            buff.pop()
            dfs(idx+1, sum)
        
        dfs(0, target)
        return res



        