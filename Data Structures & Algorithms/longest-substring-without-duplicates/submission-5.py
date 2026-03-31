class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Fixed-size array to store last seen indices
        # Initialize with -1 to distinguish from index 0
        last_seen = [-1] * 128 
        l = 0
        res = 0

        for r in range(len(s)):
            char_code = ord(s[r])
            
            # If we've seen this char and it's within the current window
            if last_seen[char_code] >= l:
                l = last_seen[char_code] + 1
            
            last_seen[char_code] = r
            res = max(res, r - l + 1)
            
        return res