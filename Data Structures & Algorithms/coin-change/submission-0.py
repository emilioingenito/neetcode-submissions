class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_change = self.change(coins, amount, {})
        return min_change if min_change != float('inf') else -1
    
    def change(self, coins: List[int], amount: int, memo: dict):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0
        
        min_change = float('inf')
        for c in coins:
            if c <= amount:
                min_change = min(min_change, 1 + self.change(coins, amount-c, memo))
        memo[amount] = min_change
        return min_change