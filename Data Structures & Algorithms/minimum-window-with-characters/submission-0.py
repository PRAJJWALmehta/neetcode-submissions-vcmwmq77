class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s): return ""

        w_count = {}
        t_count = {}

        for ch in t:
            t_count[ch] = t_count.get(ch, 0)+1
        
        have, need = 0, len(t_count)
        l = 0
        resLen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            ch = s[r]
            w_count[ch] = w_count.get(ch, 0)+1

            if ch in t_count and t_count[ch] == w_count[ch]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                ch = s[l]
                w_count[ch] -= 1
                if ch in t_count and t_count[ch] > w_count[ch]:
                    have -= 1
                l += 1
            
        
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""

