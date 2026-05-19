class Solution:
    def sumOfDigitsSquared(self, n: int) -> int:
        res = 0

        while n:
            last = n%10
            res += last**2
            n = n//10
        
        return res

    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set()

        while curr != 1:
            print(curr)
            if curr in seen:
                return False
            seen.add(curr)
            curr = self.sumOfDigitsSquared(curr)
        
        return True