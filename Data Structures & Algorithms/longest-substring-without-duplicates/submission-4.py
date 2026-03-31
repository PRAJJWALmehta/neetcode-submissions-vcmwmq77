class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0
        
        l, r = 0, 0
        arr = [0]*128
        res = 1

        while r < len(s):
            key = ord(s[r])
            if arr[key]:
                arr[ord(s[l])] = 0
                l += 1
            else:
                arr[key] = 1
                r += 1
            res = max(res, r-l)
        
        return res



