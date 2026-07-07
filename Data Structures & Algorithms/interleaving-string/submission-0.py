from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
                
            match_i =  i < len(s1) and s1[i] == s3[i+j]
            match_j =  j < len(s2) and s2[j] == s3[i+j]
            if not match_i and not match_j:
                return False
            if match_i and match_j:
                return dp(i+1, j) or dp(i, j+1)
            if match_i:
                return dp(i+1, j)
            return dp(i, j+1)
        
        return dp(0,0)