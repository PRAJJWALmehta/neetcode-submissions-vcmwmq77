class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            i = start
            tank = 0
            for _ in range(n):
                tank += gas[i%n]
                tank -= cost[i%n]
                if tank < 0:
                    break
                i += 1
            
            if i-n == start:
                return start
        
        return -1