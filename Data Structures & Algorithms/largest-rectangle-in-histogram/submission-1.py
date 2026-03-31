class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []
        i = 0

        for i in range(len(heights)):
            index = i
            while st and heights[i] < st[-1][1]:
                calcArea = st[-1][1]*(i - st[-1][0])
                maxArea = max(maxArea, calcArea)
                index = st[-1][0]
                st.pop()
            st.append([index, heights[i]])
        i += 1
        
        while st:
            calcArea = st[-1][1]*(i - st[-1][0])
            maxArea = max(maxArea, calcArea)
            st.pop()
        
        return maxArea


