import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = [], k
        for i in range(0, min(k, len(nums))):
            heapq.heappush(self.nums, nums[i])
        for i in range(k, len(nums)):
            heapq.heappushpop(self.nums, nums[i])


    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val >= self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
