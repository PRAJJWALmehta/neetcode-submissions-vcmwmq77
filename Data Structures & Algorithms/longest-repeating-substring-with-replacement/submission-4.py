class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            ind = ord(s[r]) - ord('A')
            freq[ind] += 1
            maxf = max(maxf, freq[ind])

            while (r - l + 1) - maxf > k:
                ind = ord(s[l]) - ord('A')
                freq[ind] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
