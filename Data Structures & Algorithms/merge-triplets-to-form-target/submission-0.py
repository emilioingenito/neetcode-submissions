class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        min_a = min_b = min_c = None
        
        for x, y, z in triplets:
            if x == a and y <= b and z <= c:
                min_a = x
            if x <= a and y == b and z <= c:
                min_b = y
            if x <= a and y <= b and z == c:
                min_c = c

        return None not in (min_a, min_b, min_c)