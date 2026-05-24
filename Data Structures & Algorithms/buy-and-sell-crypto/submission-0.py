class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0

        while right < len(prices): 
            while right < len(prices) and prices[left] <= prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
            
            left, right = right, right+1
        
        return max_profit


        