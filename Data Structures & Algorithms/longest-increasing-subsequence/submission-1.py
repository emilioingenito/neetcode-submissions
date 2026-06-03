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