class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.explore(nums[:-1], 0, dict()),
            self.explore(nums[1:], 0, dict())
        )


    def explore(self, nums: List[int], index: int, memo: dict) -> int:
        if index >= len(nums):
            return 0
        if index in memo:
            return memo[index]
        memo[index] = max(nums[index] + self.explore(nums, index+2, memo), self.explore(nums, index+1, memo))
        return memo[index]
        