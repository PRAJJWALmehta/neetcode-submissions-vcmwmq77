class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin, lmax = 0, 0

        for c in s:
            if c == "(":
                lmin += 1
                lmax += 1
            elif c == ")":
                lmin = max(0, lmin-1)
                lmax -= 1
                if lmax < 0:
                    return False
            else:
                lmin = max(0, lmin-1)
                lmax += 1
        
        return lmin == 0

