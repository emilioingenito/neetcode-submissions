from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices[:]
            for start, end, cost in flights:
                if prices[start] == float('inf'):
                    continue
                current_cost = prices[start] + cost
                if current_cost < tmp[end]:
                    tmp[end] = current_cost
            prices = tmp
        
        return prices[dst] if prices[dst] != float('inf') else -1
