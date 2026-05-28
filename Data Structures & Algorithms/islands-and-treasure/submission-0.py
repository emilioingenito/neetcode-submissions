from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N, M = len(grid), len(grid[0])
        starting = [((x,y), 0) for x in range(N) for y in range(M) if not grid[x][y]]
        queue, visited = deque(starting), set(pos for pos, _ in starting)
        
        while queue:
            (x, y), distance = queue.popleft()
            grid[x][y] = distance

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx+x, dy+y
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] > -1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), distance + 1))

        # Nothing to return, the grid is modified in-place
        return