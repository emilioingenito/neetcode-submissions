from collections import Counter
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        occ = Counter(nums[:k])
        heap = nums[:k][:]
        heapq.heapify_max(heap)
        ans.append(heap[0])

        for i in range(k, len(nums)):
            occ[nums[i]] += 1
            occ[nums[i-k]] -= 1
            heapq.heappush_max(heap, nums[i])
            
            while occ[heap[0]] == 0:
                heapq.heappop_max(heap)
            
            ans.append(heap[0])
        
        return ans