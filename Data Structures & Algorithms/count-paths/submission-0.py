class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.paths(m-1, n-1, {})

    
    def paths(self, m: int, n: int, memo:dict) -> int:
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0 or n == 0:
            return 1
        memo[(m, n)] = self.paths(m-1, n, memo) + self.paths(m, n-1, memo)
        return memo[(m, n)]