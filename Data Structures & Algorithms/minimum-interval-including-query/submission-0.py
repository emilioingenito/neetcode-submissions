from bisect import bisect_left
from collections import defaultdict
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted([(v, i) for i, v in enumerate(queries)])
        values = [-1] * len(queries)
        ends, i = [], 0

        for q, index in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(ends, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while ends and ends[0][1] < q:
                heapq.heappop(ends)
            if ends:
                values[index] = ends[0][0]
            
        return values