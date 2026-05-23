class Solution:
    def streak(self, values: Set[int], cache: Dict[int], value: int) -> int:
        if value not in values:
            return 0

        if value in cache:
            return cache[value]

        cache[value] = 1 + self.streak(values, cache, value + 1)
        return cache[value]


    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        values, cache = set(nums), {}
        for value in values:
            self.streak(values, cache, value)
        return max(cache.values())