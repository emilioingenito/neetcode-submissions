class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        row = self.bisect_right(matrix, 0, N, target) - 1
        return False if row < 0 else self.bs(matrix, 0, M-1, row, target)

    
    def bisect_right(self, matrix: List[List[int]], start: int, end: int, target: int) -> int:
        while start < end: 
            mid = start + (end-start)//2
            if matrix[mid][0] <= target:
                start = mid + 1
            else:
                end = mid
        return end
    

    def bs(self, matrix: List[List[int]], start: int, end: int, row:int, target: int) -> bool:
        while start <= end:
            mid = start + (end-start)//2
            value = matrix[row][mid]
        
            if value == target:
                return True
            elif value > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
