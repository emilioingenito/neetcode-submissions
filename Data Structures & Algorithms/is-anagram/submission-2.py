from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t: 
            d[c] -= 1
        return all(v == 0 for v in d.values())

        