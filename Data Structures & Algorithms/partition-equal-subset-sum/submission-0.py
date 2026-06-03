class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.partition(nums, 0, 0, sum(nums), dict())

    def partition(self, nums, index, left, total, memo):
        if (index, left) in memo:
            return memo[(index, left)]
        
        answer = False
        if index == len(nums):
            answer = total == 2 * left
        else:
            answer = self.partition(nums, index+1, left+nums[index], total, memo) or self.partition(nums, index+1, left, total, memo)
        
        memo[(index, left)] = answer
        return answer