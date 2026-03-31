class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counts = [0]*26

        for ch in s1:
            counts[ord(ch) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            key = ord(s2[r]) - ord('a')
            counts[key] -= 1

            while counts[key] < 0:
                lkey = ord(s2[l]) - ord('a')
                counts[lkey] += 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False
        