from collections import defaultdict
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = rolling = 0
        minlen = float('inf')

        for right, value in enumerate(nums):
            rolling += value
            while rolling >= target:
                minlen = min(minlen, right - left + 1)
                rolling -= nums[left]
                left += 1
        
        return minlen if minlen != float('inf') else 0