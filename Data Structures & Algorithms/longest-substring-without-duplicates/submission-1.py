class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = max_len = 0

        while right < len(s):
            while right < len(s) and s[right] not in seen: 
                seen.add(s[right])
                right += 1
            max_len = max(max_len, right - left)

            while left < right < len(s) and s[left] != s[right]:
                seen.remove(s[left])
                left += 1
            
            left += 1
            right += 1
        
        return max_len