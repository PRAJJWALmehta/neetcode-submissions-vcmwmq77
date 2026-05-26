class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ll, ul = intervals[0]
        res = []

        for interval in intervals:
            s, e = interval

            if s > ul:
                res.append([ll, ul])
                ll, ul = s, e
                continue
            
            ll = min(ll, s)
            ul = max(ul, e)
        
        res.append([ll, ul])
        return res