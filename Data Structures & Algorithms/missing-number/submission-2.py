from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ideal_xor = reduce(lambda a, b: a^b, range(len(nums)+1))
        actual_xor = reduce(lambda a, b: a^b, nums)
        return ideal_xor ^ actual_xor
        