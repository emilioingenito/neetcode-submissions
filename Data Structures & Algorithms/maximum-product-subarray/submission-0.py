class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = max_val = result = nums[0]

        for n in nums[1:]:
            values = [n, min_val * n, max_val * n]
            min_val, max_val = min(values), max(values)
            result = max(result, max_val)

        return result