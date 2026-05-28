class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def backtrack(current, index, target):
            if target == 0:
                combinations.append(current[:])
                return
            if index == len(nums) or target < 0:
                return
            
            backtrack(current + [nums[index]], index, target-nums[index])
            backtrack(current, index+1, target)

        backtrack([], 0, target)
        return combinations