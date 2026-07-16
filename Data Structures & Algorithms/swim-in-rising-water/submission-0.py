class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = [(grid[0][0], 0, 0)] # max_element, x, y
        N, M, visited = len(grid), len(grid[0]), set([(0, 0)])

        while queue:
            max_val, x, y = heapq.heappop(queue)
            if x == N-1 and y == M-1:
                return max_val          
            for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(queue, (max(max_val, grid[nx][ny]), nx, ny))
        
        return -1