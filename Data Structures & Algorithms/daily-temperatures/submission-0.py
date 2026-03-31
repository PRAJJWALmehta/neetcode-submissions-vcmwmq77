class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = deque()

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                t = st.pop()
                res[t] = i - t
            st.append(i)
        
        return res

        