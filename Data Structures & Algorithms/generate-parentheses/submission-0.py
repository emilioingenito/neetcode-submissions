class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        def backtrack(current, opened, closed):
            if opened == closed == 0:
                pairs.append(''.join(current))
                return
            
            if opened > 0:
                backtrack(current + ['('], opened-1, closed)
            if closed > 0 and closed > opened:
                backtrack(current + [')'], opened, closed-1)


        backtrack([], n, n)
        return pairs

