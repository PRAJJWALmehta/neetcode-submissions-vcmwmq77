class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s, c = 0, 1

        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + c
            c = s//10
            digits[i] = s%10
            if not c:
                break
        
        if c:
            digits = [c] + digits
        
        return digits