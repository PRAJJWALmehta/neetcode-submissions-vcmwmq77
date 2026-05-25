class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        c = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            ab = (a>>i)&1
            bb = (b>>i)&1

            s = ab^bb^c
            c = ab&bb | bb&c | c&ab

            res |= (s<<i)
        
        return -((~res&mask)+1) if (res & (1<<31)) else res