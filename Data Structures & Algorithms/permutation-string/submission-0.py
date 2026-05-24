from collections import defaultdict
class Solution:
    def createDict(self, string: str) -> dict:
        d = defaultdict(int)
        for c in string:
            d[c] += 1
        return d

    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation, current_permutation, left = self.createDict(s1), defaultdict(int), 0

        for right, value in enumerate(s2):
            if value not in permutation:
                current_permutation = defaultdict(int)
                left = right + 1
                continue
            
            current_permutation[value] +=1 
            while current_permutation[value] > permutation[value]:
                current_permutation[s2[left]] -=1 
                left += 1
            
            #(current_permutation, permutation, right, left, len(s1))
            if (right - left + 1) == len(s1) and current_permutation == permutation:
                return True
        
        return False



        