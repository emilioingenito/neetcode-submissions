import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = [[value, key] for key, value in Counter(nums).items()]
        return [key for _, key in heapq.nlargest(k, heap)]