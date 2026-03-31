class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0
        
        l, r = 0, 0
        arr = set()
        res = 1

        while r < len(s):
            if s[r] in arr:
                arr.remove(s[l])
                l += 1
            else:
                arr.add(s[r])
                r += 1
            res = max(res, r-l)
        
        return res



