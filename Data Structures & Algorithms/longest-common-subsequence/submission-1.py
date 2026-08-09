class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longest(text1, text2, 0, 0, {})

    
    def longest(self, text1: str, text2: str, i: int, j: int, memo: dict) -> int:
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(text1) or j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + self.longest(text1, text2, i+1, j+1, memo)
        else:
            memo[(i, j)] = max(
                self.longest(text1, text2, i, j+1, memo),
                self.longest(text1, text2, i+1, j, memo),
            )
        return memo[(i, j)]