class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        handmp = {}

        for i in hand:
            if i not in handmp:
                handmp[i] = 0
            handmp[i] += 1
        
        heap = list(handmp.keys())
        heapq.heapify(heap)
        
        while heap:
            first = heap[0]

            for card in range(first, first+groupSize):
                if card not in handmp:
                    return False
                
                handmp[card] -= 1
                if handmp[card] == 0:
                    if heap[0] != card:
                        return False
                    heapq.heappop(heap)
        
        return True
            
        