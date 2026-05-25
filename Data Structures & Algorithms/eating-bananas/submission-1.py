from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0
        left = 1
        right = min_speed = max(piles)
        
        while left <= right:
            mid = left + (right - left)//2
            if sum([ceil(n/mid) for n in piles]) <= h:
                right = mid - 1
                min_speed = mid
            else:
                left = mid + 1
        
        return min_speed