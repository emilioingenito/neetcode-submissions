from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, tot):
            if i == len(nums): return tot == target
            return dp(i+1, tot+nums[i]) + dp(i+1, tot-nums[i])
        
        return dp(0, 0)