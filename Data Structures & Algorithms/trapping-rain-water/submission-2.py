class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        reducedArea, res = 0, 0

        while r < len(height):
            if height[r] >= height[l]:
                res += max(0, height[l]*(r-l-1) - reducedArea)
                print(res)
                l = r
                r += 1
                reducedArea = 0
            else:
                reducedArea += height[r]
                r += 1
        
        if l != r:
            r = len(height)-1
            ptr = r
            reducedArea = 0
            while l < r:
                if height[ptr] >= height[r]:
                    res += max(0, height[r]*(r-ptr-1) - reducedArea)
                    r = ptr
                    ptr -= 1
                    reducedArea = 0
                else:
                    reducedArea += height[ptr]
                    ptr -= 1

        return res

        