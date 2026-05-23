N = 9
class Solution:
    def invalidList(self, board: List[List[str]], x:int, y: int, horizontal: bool):
        numbers = [] 

        while 0 <= x < N and 0 <= y < N:
            if board[x][y] != '.':
                numbers.append(board[x][y])
            if horizontal:
                y += 1
            else:
                x += 1
        
        return len(numbers) != len(set(numbers))


    def invalidBox(self, board: List[List[str]], x:int, y: int):
        numbers = []

        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != '.':
                    numbers.append(board[i][j])
        
        return len(numbers) != len(set(numbers))           


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for x in range(N):
            if self.invalidList(board, x, 0, True):
                return False
        
        # Check each column
        for y in range(N):
            if self.invalidList(board, 0, y, False):
                return False
        
        # Check each box
        for x in range(0, N, 3):
            for y in range(0, N, 3):
                if self.invalidBox(board, x, y):
                    return False
        
        # All checks passed
        return True