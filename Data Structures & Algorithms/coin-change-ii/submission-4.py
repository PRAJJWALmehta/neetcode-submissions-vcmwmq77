class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, amt):
            if amt == amount:
                return 1
            if i >= len(coins) or amt > amount:
                return 0
            
            if (i, amt) not in dp:
                dp[(i, amt)] = dfs(i, amt+coins[i]) + dfs(i+1, amt)
            
            return dp[(i, amt)]
        
        return dfs(0, 0)