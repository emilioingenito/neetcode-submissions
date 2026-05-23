from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        zeros = nums.count(0)
        
        if zeros == 1:
            total = 1
            for num in nums:
                total *= num if num != 0 else 1
            return [0 if num != 0 else total for num in nums]
        
        elif zeros > 1:
            return [0] * len(nums)
        
        else:
            total = prod(nums)
            return [int(total/num) for num in nums]
        