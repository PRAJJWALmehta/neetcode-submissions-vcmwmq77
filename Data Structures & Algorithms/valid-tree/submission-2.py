class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [0]*n
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            if a == b:
                return False
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, parent):
            if visited[node] == 1:
                print(node)
                return False
            
            visited[node] = 1

            for adj in adjList[node]:
                if adj != parent and not dfs(adj, node):
                    return False

            visited[node] = -1
            
            return True
    
        if not dfs(0, -1):
            return False
        for node in range(1, n):
            if not visited[node]:
                return False
        
        return True
        