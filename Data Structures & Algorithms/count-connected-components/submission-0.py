class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        preMap = {i: [] for i in range(n)}
        for a, b in edges:
            preMap[a].append(b)
            preMap[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for i in preMap[node]:
                dfs(i)

        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res