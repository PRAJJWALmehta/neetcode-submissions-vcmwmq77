class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1

        while l <= r:
            key = l + (r-l)//2
            val = matrix[key//n][key%n]

            if val > target:
                r = key-1
            elif val < target:
                l = key+1
            else:
                return True
        
        return False