class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTriplets = []
        isTarget = [False, False, False]

        for t in triplets:
            a, b, c = t
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    isTarget[0] = True
                if b == target[1]:
                    isTarget[1] = True
                if c == target[2]:
                    isTarget[2] = True

                validTriplets.append(t)
        
        return isTarget[0] and isTarget[1] and isTarget[2]



