class StockSpanner:

    def __init__(self):
        self.prices = [] # (price, streak)
        

    def next(self, price: int) -> int:
        streak = 1
        while self.prices and price >= self.prices[-1][0]:
            streak += self.prices.pop()[1]
        self.prices.append((price, streak))
        return streak

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)