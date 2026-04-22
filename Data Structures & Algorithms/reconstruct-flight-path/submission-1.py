class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        res = ["JFK"]        

        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        
        def dfs(src):
            if len(tickets)+1 == len(res):
                return True
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                if v == "-1":
                    continue

                res.append(v)
                adj[src][i] = "-1"

                if dfs(v):
                    return True
                
                res.pop()
                adj[src][i] = v
                
        dfs("JFK")
        return res