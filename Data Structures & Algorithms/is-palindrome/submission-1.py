class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(s)-1
        print(s)
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        
        return True
