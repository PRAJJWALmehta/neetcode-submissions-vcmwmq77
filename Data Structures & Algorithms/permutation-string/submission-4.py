class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        counts = [0] * 26
        for ch in s1:
            counts[ord(ch) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            key = ord(s2[r]) - ord('a')
            counts[key] -= 1
            
            # If counts[key] < 0, we have either:
            # 1. A character not in s1
            # 2. Too many of a character that IS in s1
            # Shrink from the left until counts[key] is 0 again.
            while counts[key] < 0:
                counts[ord(s2[l]) - ord('a')] += 1
                l += 1
            
            # If the window size matches s1, we found it!
            if r - l + 1 == len(s1):
                return True
                
        return False