class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanS = "".join(filter(str.isalnum, s)).lower()
        first, last = 0, len(cleanS)-1

        while first < last:
            if cleanS[first] != cleanS[last]:
                return False
            first += 1
            last -= 1
        
        return True
        