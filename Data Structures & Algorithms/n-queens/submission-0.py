class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        valid_boards = self.solve_recursive(n, 0, [], set(), set(), set())
        for res in valid_boards:
            board.append(self.create_qboard(res, n))
        return board
    
    def solve_recursive(self, N: int, r: int, ans:List, cols: set, diag1: set, diag2: set) -> List[List[str]]:
        if r == N:
            return [ans] if len(ans) == N else []
        
        valid_res = []
        for c in range(N):
            if c not in cols and (r-c) not in diag1 and (r+c) not in diag2:
                valid_res.extend(self.solve_recursive(N, r+1, ans + [c], cols | {c}, diag1 | {r-c}, diag2 | {r+c}))
        
        return valid_res
    
    def create_qboard(self, board, N):
        ans = []
        for e in board:
            curr = ['.'] * N
            curr[e] = 'Q'
            ans.append(''.join(curr))
        return ans