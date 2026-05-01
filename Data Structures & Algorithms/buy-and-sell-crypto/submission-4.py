class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            buy = prices[l]
            if prices[l] <= prices[r]:
                buy = min(buy, prices[l])
                cur_profit = prices[r] - buy
                profit = max(cur_profit, profit)
                r += 1
            else:
                l = r
                r += 1
        
        return profit



        

        


