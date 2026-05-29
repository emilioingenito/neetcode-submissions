from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N, M = len(heights), len(heights[0])

        def bfs(queue, reachable_set):
            while queue:
                x, y = queue.popleft()
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in reachable_set and heights[nx][ny] >= heights[x][y]:
                        reachable_set.add((nx, ny))
                        queue.append((nx, ny))
        
        pacific = [(0, y) for y in range(M)] + [(x, 0) for x in range(N)]
        atlantic = [(N-1, y) for y in range(M)] + [(x, M-1) for x in range(N)]
        reachable_pacific, reachable_atlantic = set(pacific), set(atlantic)
        bfs(deque(pacific), reachable_pacific)
        bfs(deque(atlantic), reachable_atlantic)

        return list(map(lambda position: list(position), reachable_pacific & reachable_atlantic))

                        



