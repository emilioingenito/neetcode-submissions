class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        L, R, B, T = 0, M-1, N-1, 0
        ans = []
        
        while L <= R and T <= B:
            for col in range(L, R+1):
                ans.append(matrix[T][col])
            T+=1

            for row in range(T, B+1):
                ans.append(matrix[row][R])
            R -=1

            if T <= B:
                for col in range(R, L-1, -1):
                    ans.append(matrix[B][col])
                B -= 1
            
            if L <= R:
                for row in range(B, T-1, -1):
                    ans.append(matrix[row][L])
                L += 1
        
        return ans
