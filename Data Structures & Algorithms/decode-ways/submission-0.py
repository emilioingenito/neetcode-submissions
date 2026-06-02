class Solution:
    def numDecodings(self, s: str) -> int:
        return self.ways(s, 0, {})
    
    
    def ways(self, s:str, index:int, memo: dict) -> int:
        if index in memo:
            return memo[index]

        if index == len(s):
            return 1
        
        if s[index] == '0':
            return 0
        
        total = self.ways(s, index+1, memo)
        if index < len(s)-1 and int(s[index:index+2]) <= 26:
            total += self.ways(s, index+2, memo)
        memo[index] = total
        return total
        