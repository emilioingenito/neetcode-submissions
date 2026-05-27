class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, islands = set(), 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=='1' and (x, y) not in visited:
                    islands += 1
                    self.expand(grid, x, y, visited)

        
        return islands


    def expand(self, grid: List[List[str]], start: int, end: int, visited: set) -> None:
        queue = [(start, end)]
        print(queue)
        while queue:
            x, y = queue.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1, 0), (+1, 0), (0, +1), (0, -1)]:
                next_x, next_y = x+dx, y+dy
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y]=='1':
                    queue.append((next_x, next_y))
                print(queue)
        return
