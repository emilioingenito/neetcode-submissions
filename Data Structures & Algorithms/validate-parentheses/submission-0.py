class Solution:
    def isValid(self, s: str) -> bool:
        opened, closed, idx, stack = '([{', '}])', 0, []
        valid_pairs = set(['()', '[]', '{}'])

        for char in s:
            if char in opened:
                stack.append(char)
                continue
            
            if not stack or stack[-1] + char not in valid_pairs:
                return False
            
            stack.pop()
        
        return not stack


        