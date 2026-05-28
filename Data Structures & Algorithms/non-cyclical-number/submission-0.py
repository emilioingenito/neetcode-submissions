class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = self.squaresSum(n)

        return True
    

    def squaresSum(self, n: int) -> int:
        ans, iteration = 0, len(str(n))-1
        while iteration > -1:
            ans += ((n//10**iteration) % 10) ** 2
            iteration -= 1
        return ans
