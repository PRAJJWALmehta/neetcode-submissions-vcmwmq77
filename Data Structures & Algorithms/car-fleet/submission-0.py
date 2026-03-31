class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        
        cars = sorted(cars, reverse=True)

        st = []

        for i in range(len(cars)):
            arrival_time = (target - cars[i][0])/cars[i][1]
            if not st:
                st.append(arrival_time)
            else:
                if st[-1] < arrival_time:
                    st.append(arrival_time)

        
        return len(st)