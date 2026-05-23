from math import prod
from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
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
            return [total//num for num in nums]
        '''


        '''
        1 2 4 6

        [1 1 2 8]
        [48 24 6 1]

        LEFT:   1  1  2  8 48
        RIGHT: 48 48 24 6  1
        '''
        left, right, product = [1], deque([1]), []
        for n in nums[:-1]:
            left.append(left[-1] * n)
        for n in reversed(nums[1:]):
            right.appendleft(right[0] * n)

        for i in range(len(nums)):
            product.append(left[i] * right[i])

        return product