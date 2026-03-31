class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(filter(str.isalnum, s)).lower()

        if cleanString[::-1] == cleanString:
            return True
        else:
            return False
        