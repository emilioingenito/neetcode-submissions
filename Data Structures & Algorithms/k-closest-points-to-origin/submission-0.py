import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(sqrt(point[0]**2+point[1]**2), point) for point in points]
        k_closest = heapq.nsmallest(k, distances)
        return [point for _, point in k_closest]