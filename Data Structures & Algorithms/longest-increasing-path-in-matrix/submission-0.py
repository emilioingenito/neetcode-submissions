class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        longestPath, memo = 0, {}
        for i in range(N):
            for j in range(M):
                if (i, j) not in memo:
                    longestPath = max(longestPath, self.search(matrix, i, j, memo))
        return longestPath + 1

    def search(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 0

        longestPath = 0
        for x, y in [[i-1, j],[i+1, j],[i, j-1],[i, j+1]]:
            if self.inBound(x, y, len(matrix), len(matrix[0])) and matrix[i][j] < matrix[x][y]:
                longestPath = max(longestPath, 1 + self.search(matrix, x, y, memo))
        memo[(i, j)] = longestPath
        return longestPath
    
    def inBound(self, i, j, N, M):
        return 0 <= i < N and 0 <= j < M