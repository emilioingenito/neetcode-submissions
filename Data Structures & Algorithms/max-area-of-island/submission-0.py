class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, visited = 0, set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and grid[x][y]:
                    visited.add((x, y))
                    max_area = max(max_area, self.expandArea(grid, x, y, set([(x,y)])))
        return max_area


    def expandArea(self, grid: List[List[int]], x:int, y: int, visited: set) -> int:
        area = 1
        for (dx, dy) in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] and (nx, ny) not in visited:
                visited.add((nx, ny))
                area += self.expandArea(grid, nx, ny, visited)
        return area
        