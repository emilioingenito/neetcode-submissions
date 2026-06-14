class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.ways(amount, coins, 0, dict())
        

    def ways(self, amount: int, coins: List[int], index: int, memo: dict) -> int:
        if (amount, index) in memo:
            return memo[(amount, index)]
        if amount < 0:
            return 0
        if index == len(coins):
            return 1 if amount == 0 else 0
        memo[(amount, index)] = self.ways(amount-coins[index], coins, index, memo) + self.ways(amount, coins, index+1, memo)
        return memo[(amount, index)]