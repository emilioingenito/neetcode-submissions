from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for idx, n in enumerate(nums): 
            if n in d:
                return [d[n], idx]
            d[target - n] = idx
        raise Exception('Malformed inpu')