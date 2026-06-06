class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.distance(word1, word2, 0, 0, {})
    

    def distance(self, word1: str, word2: str, index1:int, index2, memo:dict) -> int:
        if (index1, index2) in memo:
            return memo[(index1, index2)]

        if index1 == len(word1) or index2 == len(word2):
            return len(word2) - index2 + len(word1) - index1
        
        if word1[index1] == word2[index2]:
            memo[(index1, index2)] = self.distance(word1, word2, index1+1, index2+1, memo)
        else:
            memo[(index1, index2)] = 1 + min(
                self.distance(word1, word2, index1+1, index2+1, memo), # replace
                self.distance(word1, word2, index1+1, index2, memo),   # delete
                self.distance(word1, word2, index1, index2+1, memo)    # insert
            )
        return memo[(index1, index2)]