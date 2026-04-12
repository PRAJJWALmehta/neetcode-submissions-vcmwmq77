from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Optimization 1: Fundamental Tree Property
        # A valid tree MUST have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False
            
        # Optimization 2: Simplified Adjacency List
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def has_cycle(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                # If neighbor already visited, we found a cycle
                if neighbor in visited or has_cycle(neighbor, node):
                    return True
            return False

        # Start DFS. If cycle found, or not all nodes reachable, it's not a tree.
        # Note: If len(edges) == n-1 and there's no cycle, 
        # it is mathematically guaranteed to be connected.
        return not has_cycle(0, -1) and len(visited) == n