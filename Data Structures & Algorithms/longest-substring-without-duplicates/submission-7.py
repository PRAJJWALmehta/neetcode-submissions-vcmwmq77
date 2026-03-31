class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        last_seen = [-1]*128
        l = 0

        for r in range(len(s)):
            key = ord(s[r])
            if last_seen[key] >= l:
                l = last_seen[key]+1
            last_seen[key] = r
            res = max(res, r - l + 1)
        
        return res