class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return True
        N, M = len(board), len(board[0])
        return any(self.find(board, word, x, y, 0, set([(x, y)])) for x in range(N) for y in range(M))
    

    def find(self, board: List[List[str]], word: str, x: int, y: int, index: int, visited: set) -> bool:
        if index == len(word)-1 and board[x][y]==word[index]:
            return True
        
        if board[x][y] != word[index]:
            return False
        
        found = False
        for dx, dy in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                visited.add((nx, ny))
                found |= self.find(board, word, nx, ny, index+1, visited)
                visited.remove((nx, ny))
        return found