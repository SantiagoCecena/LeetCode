class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        buy2 = -prices[0]
        profit1 = 0
        total_profit = 0

        for price in prices:
            buy1 = max(buy1,-price)
            profit1 = max(profit1, price + buy1)
            buy2 = max(buy2,profit1 - price)
            total_profit = max(total_profit, price + buy2)
        return total_profit
