class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, solution = 0, 0
        for index, (current_gas, current_cost) in enumerate(zip(gas, cost)):
            total += current_gas - current_cost
            if total < 0:
                solution, total = index + 1, 0
        return solution if sum(g-c for g,c in zip(gas, cost)) >= 0 else -1