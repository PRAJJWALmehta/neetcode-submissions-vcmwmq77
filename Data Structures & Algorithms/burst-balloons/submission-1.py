class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) not in dp:
                dp[(l, r)] = 0
                for i in range(l, r+1):
                    coins = arr[l-1]*arr[i]*arr[r+1]
                    coins += dfs(l, i-1) + dfs(i+1, r)
                    dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]
        
        return dfs(1, len(arr)-2)