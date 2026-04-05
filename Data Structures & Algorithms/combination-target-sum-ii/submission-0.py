class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        buff = []

        candidates.sort()

        def dfs(i: int, sum: int):
            if not sum:
                res.append(buff.copy())
                return
            if i >= len(candidates) or sum < 0:
                return
            
            buff.append(candidates[i])
            dfs(i+1, sum-candidates[i])
            buff.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, sum)
        
        dfs(0, target)
        return res
    

            
        