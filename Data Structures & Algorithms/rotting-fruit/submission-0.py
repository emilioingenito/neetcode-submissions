from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M, steps = len(grid), len(grid[0]), 0

        rotten = [(x, y) for x in range(N) for y in range(M) if grid[x][y]==2]
        queue, visited = deque(rotten), set(rotten)

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                    if 0<= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            steps += 1
        
        unreached_fresh = any([(x, y) not in visited for x in range(N) for y in range(M) if grid[x][y]==1])
        return -1 if unreached_fresh else max(0, steps-1)