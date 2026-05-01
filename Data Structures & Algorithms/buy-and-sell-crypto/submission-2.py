class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        r = 1
        
        while r < len(prices):
            buy = prices[l]
            while r < len(prices) and prices[l] <= prices[r]:
                buy = min(buy, prices[l])
                cur_profit = prices[r] - buy
                profit = max(cur_profit, profit)
                print("profit: ", profit)
                r += 1
            l = r
            r += 1
        
        return profit



        

        


