class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N, M = len(matrix), len(matrix[0])
        first_row = any(matrix[0][y] == 0 for y in range(M))
        first_col = any(matrix[x][0] == 0 for x in range(N))

        for x in range(N):
            for y in range(M):
                if not matrix[x][y]:
                    matrix[0][y] = 0
                    matrix[x][0] = 0
        
        for y in range(1, M):
            if not matrix[0][y]:
                for x in range(N):
                    matrix[x][y]=0

        for x in range(1, N):
            if not matrix[x][0]:
                for y in range(M):
                    matrix[x][y] = 0

        if first_row:
            matrix[0] = [0] * M
        if first_col:
            for x in range(N):
                matrix[x][0] = 0
        
        # In-place modification, nothing to return
        return
        
        