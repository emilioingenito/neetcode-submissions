class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0
        for index in range(len(s)):
            substrings += self.expand(s, index, index)
            substrings += self.expand(s, index, index+1)
        return substrings


    def expand(self, s: str, l:int, r:int) ->int:
        substrings=0
        while 0 <= l and r < len(s) and s[l] == s[r]:
            substrings += 1
            l -=1
            r +=1
        return substrings  