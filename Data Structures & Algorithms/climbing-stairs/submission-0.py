class Solution:
    def climbStairs(self, n: int) -> int:
        prev, last, current = 0, 1, 0
        for _ in range(n):
            current = prev + last
            prev, last = last, current
        return current
        
        