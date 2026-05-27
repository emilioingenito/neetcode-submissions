class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = []
        for n in nums:
            if k > 0:
                heapq.heappush(kth, n)
                k -= 1
            elif n > kth[0]:
                heapq.heappushpop(kth, n)
        return kth[0]
        