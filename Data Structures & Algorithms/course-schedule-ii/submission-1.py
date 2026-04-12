class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = list()
        visited = [0]*numCourses
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(course):
            if visited[course] == 1:
                return False
            if preMap[course] == []:
                if visited[course] == 0:
                    print(course)
                    res.append(course)
                    visited[course] = -1
                return True
            
            visited[course] = 1

            for crs in preMap[course]:
                if not dfs(crs):
                    return False

            if visited[course] == 1:
                print(course)
                res.append(course)
            visited[course] = -1
            preMap[course] = []
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res