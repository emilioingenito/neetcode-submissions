class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev_t, prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx

            stack.append([t, idx])
        
        return result
        