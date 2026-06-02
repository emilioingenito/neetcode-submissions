class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.words(s, wordDict, 0, {})
    

    def words(self, s: str, wordDict: List[str], index:int, memo: dict) -> bool:
        if index in memo:
            return memo[index]

        if index == len(s):
            return True
        
        memo[index] = False
        for word in wordDict:
            if s[index:].startswith(word) and self.words(s, wordDict, index+len(word), memo):
                memo[index] = True
                break
        return memo[index]