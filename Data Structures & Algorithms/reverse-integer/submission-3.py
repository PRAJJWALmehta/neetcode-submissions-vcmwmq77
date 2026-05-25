class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        n = int(math.log10(x))
        res = 0

        
        for i in range(n+1):
            d = x%10
            res += d*pow(10, n-i)
            x = x//10

        if res >= pow(2, 31):
            return 0

        return res*pow(-1, int(neg))