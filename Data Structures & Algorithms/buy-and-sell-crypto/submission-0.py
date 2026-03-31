class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = float('inf')

        for sell_price in prices:
            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)
            if sell_price < buy_price:
                buy_price = sell_price        
        
        return int(max_profit)
        