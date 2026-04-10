"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        res = None
        nodeMap = defaultdict()
        q = deque()

        q.append(node)

        # create clones of the original graph 
        # then map the old nodes to the cloned nodes
        while q:
            curr = q.popleft()
            if curr in nodeMap:
                continue
            clone = Node(curr.val)
            nodeMap[curr] = clone

            for neighbor in curr.neighbors:
                if neighbor not in nodeMap:
                    q.append(neighbor)
        
        # traverse the graph again but use original graph as reference to connect the new cloned nodes

        q.append(node)
        visited = set()

        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            clone = nodeMap[curr]
            visited.add(curr)

            for neighbor in curr.neighbors:
                clone.neighbors.append(nodeMap[neighbor])
                if neighbor not in visited:
                    q.append(neighbor)

        res = nodeMap[node]
        return res
        
        