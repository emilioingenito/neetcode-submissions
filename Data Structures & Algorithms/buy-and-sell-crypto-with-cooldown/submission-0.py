class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.profit(prices, 0, False, {})


    def profit(self, prices: List[int], index: int, can_sell: bool, memo:dict) -> int:
        if (index, can_sell) in memo:
            return memo[(index, can_sell)]

        if index >= len(prices):
            return 0

        # 1. I cannot sell, I either buy or skip the current
        if not can_sell:
            memo[(index, can_sell)] = max(
                -prices[index] + self.profit(prices, index+1, True, memo), # Buy
                self.profit(prices, index+1, False, memo)              # Not buy
            )
        
        # 2. I can only sell
        else:
            memo[(index, can_sell)] = max(
                prices[index] + self.profit(prices, index+2, False, memo), # Sell now
                self.profit(prices, index+1, True, memo)                   # Sell later
            )
        
        return memo[(index, can_sell)]