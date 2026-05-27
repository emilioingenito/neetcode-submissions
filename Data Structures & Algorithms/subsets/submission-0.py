class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(ans, index):
            nonlocal result
            
            if index == len(nums):
                result.append(ans[:])
                return
            
            backtrack(ans + [nums[index]], index+1)
            backtrack(ans, index+1)
        
        backtrack([], 0)
        return result