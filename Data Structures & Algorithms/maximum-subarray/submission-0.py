class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for n in nums:
            current_sum += n
            max_sum = max(max_sum, current_sum)
            current_sum = 0 if current_sum < 0 else current_sum
        
        return max_sum
        