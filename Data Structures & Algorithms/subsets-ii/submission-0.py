class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()

        def backtrack(current, index):
            if index == len(nums):
                subsets.append(current[:])
                return
            
            backtrack(current + [nums[index]], index+1)
            index += 1
            while index < len(nums) and nums[index] == nums[index-1]:
                index += 1
            backtrack(current, index)

        backtrack([], 0)
        return subsets