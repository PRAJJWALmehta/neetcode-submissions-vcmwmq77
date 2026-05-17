class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rangeMap = {}
        res = []

        for i in range(len(s)):
            if s[i] not in rangeMap:
                rangeMap[s[i]] = [i, i]
            rangeMap[s[i]][1] = i
        
        ll, ul = 0, 0
        for key, val in rangeMap.items():
            l, u = val
            if l > ul:
                res.append(ul-ll+1)
                ll = l
            ul = max(ul, u)
        
        res.append(ul-ll+1)
        return res



