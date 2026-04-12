class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            
            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            
            visited.remove(course)
            preMap[course] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True