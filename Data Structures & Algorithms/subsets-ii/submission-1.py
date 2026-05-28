class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()

        def backtrack(current, index):
            if index == len(nums):
                subsets.append(current[:])
                return
            
            backtrack(current + [nums[index]], index+1)
            while index+1 < len(nums) and nums[index+1] == nums[index]:
                index += 1
            backtrack(current, index+1)

        backtrack([], 0)
        return subsets