class Solution:
    def timeToEatBananas(self, piles: List[int], k: int) -> int:
        count = 0
        for val in piles:
            count += val//k + (val%k != 0)
        
        return count



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        piles.sort()

        while l <= r:
            k = l + (r-l)//2
            timeTaken = self.timeToEatBananas(piles, k)

            if timeTaken <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        
        return res





