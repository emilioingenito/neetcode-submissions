from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited, N, M = set(), len(board), len(board[0])

        for x in range(N):
            for y in range(M):
                if (x, y) not in visited and board[x][y] == 'O':
                    visited.add((x, y))
                    self.bfs(board, x, y, visited)
        
        # Nothing to return, changes are done in-place
        return

    
    def in_board(self, x: int, y: int, N: int, M: int):
        return x != 0 and x != N-1 and y != 0 and y != M-1


    def bfs(self, board: List[List[str]], x: int, y: int, visited: set) -> None:
        N, M = len(board), len(board[0])
        to_be_colored, queue, surrounded = set([(x, y)]), deque([(x, y)]), self.in_board(x,y,N,M)

        while queue:
            x, y = queue.popleft()
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and board[nx][ny] == 'O':
                    to_be_colored.add((nx, ny))
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    surrounded &= self.in_board(nx, ny, N, M)

        if surrounded:
            for (x, y) in to_be_colored:
                board[x][y] = 'X'
        
        return

