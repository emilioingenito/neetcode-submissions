class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = last = 0
        for i in range(2, len(cost)+1):
            prev, last = last, min(prev+cost[i-2], last+cost[i-1])
        return last
