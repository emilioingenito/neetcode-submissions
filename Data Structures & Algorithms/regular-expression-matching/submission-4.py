from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dp(x, y):
            if x == len(s) or y == len(p):
                return x == len(s) and (len(p[y:])%2==0 and all(k=='*' for k in [v for i, v in enumerate(p[y:]) if i%2!=0]))

            match = False
            if p[y+1:y+2] == '*':
                match |= dp(x, y+2)
                while x < len(s) and (s[x] == p[y] or (p[y] == '.')):
                    match |= dp(x+1, y+2)
                    x += 1
            elif p[y] == '.' or s[x] == p[y]:
                match |= dp(x+1, y+1)
            return match

        return dp(0, 0)