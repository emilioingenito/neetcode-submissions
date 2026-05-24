from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_len = 0
        seen = defaultdict(int)

        for right, n in enumerate(s): 
            seen[n] += 1

            while (right - left + 1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len