class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        MAP = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz', 
        }
        
        combinations = []

        def backtrack(current, index):
            if index == len(digits):
                combinations.append(''.join(current))
                return
            
            for s in MAP[digits[index]]:
                current.append(s)
                backtrack(current, index+1)
                current.pop()


        backtrack([], 0)
        return combinations