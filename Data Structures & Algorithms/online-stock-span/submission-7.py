class StockSpanner:

    def __init__(self):
        self.mon_stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.mon_stack and self.mon_stack[-1][0] <= price:
            span += self.mon_stack.pop()[1]

        self.mon_stack.append((price, span))

        return span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)