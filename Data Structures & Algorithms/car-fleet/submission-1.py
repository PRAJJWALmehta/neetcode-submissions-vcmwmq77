class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        st = []

        for i in range(len(cars)):
            arrival_time = (target - cars[i][0])/cars[i][1]
            if not st:
                st.append(arrival_time)
            else:
                if st[-1] < arrival_time:
                    st.append(arrival_time)

        
        return len(st)