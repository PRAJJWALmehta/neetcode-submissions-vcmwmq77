class Solution:
    def topoSort(self, adj):
        res = []
        q = deque()
        indegree = {c: 0 for c in adj}
        
        for c in adj:
            for node in adj[c]:
                indegree[node] += 1
        
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        
        if len(adj) != len(res):
            return ""
        
        return res
            
        



    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] == w2[j]:
                    continue
                adj[w1[j]].add(w2[j])
                break
        
        res = self.topoSort(adj)

        return "".join(res)
            