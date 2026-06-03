class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.length(nums, 0, None, {})

    def length(self, nums: List[int], index: int, prev: int, memo: dict) -> int:
        if (index, prev) in memo:
            return memo[index, prev]

        if index == len(nums):
            return 0
        
        longest = 0 
        if prev is None or nums[index] > prev:
            longest = max(longest, 1 + self.length(nums, index+1, nums[index], memo))
        longest = max(longest, self.length(nums, index+1, prev, memo))
        memo[(index, prev)] = longest
        return longest


    def bottom_up(self, nums) -> int:
        dp = [1] * len(nums)
        for index in range(1, len(nums)):
            for prev in range(index):
                if nums[index] > nums[prev]:
                    dp[index] = max(dp[index], dp[prev]+1)
        return max(dp) 