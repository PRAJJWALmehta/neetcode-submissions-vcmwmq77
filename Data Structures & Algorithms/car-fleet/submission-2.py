class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        prev_time = 0
        fleets = 1

        for i in range(len(cars)):
            arrival_time = (target - cars[i][0])/cars[i][1]
            if not prev_time:
                prev_time = arrival_time
            else:
                if prev_time < arrival_time:
                    prev_time = arrival_time
                    fleets += 1

        
        return fleets