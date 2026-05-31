class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        def iterate(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l-1, r+1
            return l, r
            
        for i in range(len(s)):
            l, r = iterate(i-1, i+1)
            longest = s[l+1:r] if (r-l) > len(longest) else longest
            l, r = iterate(i, i+1)
            longest = s[l+1:r] if (r-l) > len(longest) else longest

        return longest