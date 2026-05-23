import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        heap = [[value, key] for key, value in Counter(nums).items()]
        return [key for _, key in heapq.nlargest(k, heap)]
        '''

        d = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)] 

        for key, value in d.items():
            buckets[value].append(key)
        
        i = len(buckets)-1
        ans = []

        while k > 0:
            ans.extend(buckets[i])
            k -= len(buckets[i])
            i -= 1
        return ans
            
