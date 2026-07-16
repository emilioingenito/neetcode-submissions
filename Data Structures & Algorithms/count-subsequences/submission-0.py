from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dp(x, y):
            if y == len(t):
                return 1
            if x == len(s):
                return 0
            if s[x] == t[y]:
                return dp(x+1, y+1) + dp(x+1, y)
            return dp(x+1, y)
        
        return dp(0, 0)